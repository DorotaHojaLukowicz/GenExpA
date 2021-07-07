import numpy as np
import pandas as pd

def normfinder(dat0, textfile=None, ctVal=False, pStabLim=0.25):
    if textfile:
        dat0 = pd.read_csv(textfile, index_col=0, sep=r"\s+")
    
    # ----------------------
    ntotal = dat0.shape[1]
    k0 = dat0.shape[0]

    ngenes = k0-1
    genenames = dat0.index[:-1]
    grId = dat0.values[-1].astype(int)

    dat = dat0.values[:-1]

    if not ctVal:
        dat = np.log2(dat)
    uq_grId = np.unique(grId)
    ngr = len(uq_grId)

    nsamples = []
    for _id in uq_grId:
        _shape = dat[:,grId == _id].shape
        nsamples.append(_shape[1])
    nsamples = np.array(nsamples)

    # MakeStab(dat)
    da = dat

    sampleavg = np.mean(dat, axis=0)

    genegroupavg = []
    groupavg = []

    # Group averages
    for gr_id in uq_grId:
        gr_ave = np.mean(dat[:, grId == gr_id], axis=1)
        genegroupavg.append(gr_ave)
        groupavg.append(np.mean(gr_ave))

    genegroupavg = np.array(genegroupavg).T
    groupavg = np.array(groupavg)


    # Variances
    GGvar = np.zeros((ngenes, ngr))
    for group_index, gr_name in enumerate(uq_grId):
        grset = grId == gr_name
        a = np.zeros(ngenes)

        for gene_index in range(ngenes):
            a[gene_index] = np.sum(
                (da[gene_index, grset]
                - genegroupavg[gene_index, group_index]
                - sampleavg[grset]
                + groupavg[group_index])**2)/ (nsamples[group_index]-1)

        GGvar[:,group_index] = (a-np.sum(a)/(ngenes*ngenes-ngenes))/(1-2/ngenes)


    # Change possible negative values
    genegroupMinvar = np.zeros((ngenes, ngr))
    for group_index, gr_name in enumerate(uq_grId):
        grset = grId == gr_name
        z = da[:,grset]

        for gene_index in range(ngenes):
            varpair = np.zeros(ngenes, dtype=float)
            for gene1_index in range(ngenes):
                varpair[gene1_index] = np.var(z[gene_index,:]-z[gene1_index,:], ddof=1)

            genegroupMinvar[gene_index, group_index] = np.min(varpair[np.arange(ngenes) != gene_index])/4.0


    # Final variances
    GGvar[GGvar < 0] = genegroupMinvar[GGvar < 0]

    # Old stability measure for each gene is calculated:
    dif = genegroupavg
    difgeneavg = np.mean(dif, axis=1)
    difgroupavg = np.mean(dif, axis=0)
    difavg = np.mean(dif)

    for gene_index in range(ngenes):
        for group_index in range(ngr):
            dif[gene_index, group_index] = (dif[gene_index, group_index]
                                            -difgeneavg[gene_index]
                                            -difgroupavg[group_index]
                                            +difavg)

    nsampMatrix = np.tile(nsamples, (ngenes, 1))
    vardif = GGvar/nsampMatrix

    gamma = np.sum(dif*dif)/((ngr-1)*(ngenes-1))-np.sum(vardif)/(ngenes*ngr)
    gamma = max(gamma, 0)

    difnew = dif*gamma/(gamma+vardif)
    varnew = vardif+gamma*vardif/(gamma+vardif)
    Ostab0 = np.abs(difnew)+np.sqrt(varnew)
    Ostab = np.mean(Ostab0, axis=1)

    # Measure of group differences:
    mud = np.zeros(ngenes)
    for gene_index in range(ngenes):
        mud[gene_index] = 2.0*np.max(np.abs(dif[gene_index,:]))

    # Common variance:
    genevar = np.zeros(ngenes)
    for gene_index in range(ngenes):
        genevar[gene_index] = np.sum((nsamples-1)*GGvar[gene_index,:])/(np.sum(nsamples)-ngr)


    Gsd = np.sqrt(genevar)
    results = [mud, Gsd, Ostab, np.ones(ngenes)*gamma, GGvar, dif]
    results = np.column_stack(results)


    # END MAKE STAB DEFINITION

    # MakeComb2

    def MakeComb2(g1, g2, res):
        gam = res[0,3]

        d1 = res[g1, (4+ngr):(4+ngr+ngr)]
        d2 = res[g2, (4+ngr):(4+ngr+ngr)]
        s1 = res[g1, 4:(4+ngr)]
        s2 = res[g2, 4:(4+ngr)]

        try:
            rho = np.abs(gam*d1/(gam+s1/nsamples)+
                    gam*d2/(gam+s2/nsamples))*np.sqrt(ngenes/(ngenes-2) )/2.0
        except ZeroDivisionError:
            print("TTEST")
            print("(gam+s1/nsamples):{}".format(gam+s1/nsamples))
            print("(gam+s2/nsamples):{}".format(gam+s2/nsamples))
            print("(ngenes-2):{}".format(ngenes-2))
            raise ValueError("val")
        rho = rho + np.sqrt(s1/nsamples+gam*s1/(nsamples*gam+s1) +
                        s2/nsamples+gam*s2/(nsamples*gam+s2))/2

        return np.mean(rho)

    # Main part
    res = results

    #gcand = np.arange(ngenes)[res[:,2]<pStabLim]
    gcand = np.arange(ngenes)[res[:,2] > -np.inf]
    ncand = len(gcand)

    if ncand < 4 :
        if ngenes > 3:
            li = sorted(res[:,2])[3]
            gcand = np.arange(ngenes)[res[:,2] <= li]
            ncand = len(gcand)
        else:
            gcand = np.arange(ngenes)
            ncand = len(gcand)

    vv2 = []
    for g1 in range(ncand-1):
        for g2 in range(g1+1, ncand):
            qmeas = MakeComb2(gcand[g1], gcand[g2], res)

            vv2.append([gcand[g1], gcand[g2], qmeas])

    # return preparation
    vv2_sorted = sorted(vv2, key = lambda x: x[2])
    vv2_named = [[genenames[_[0]], genenames[_[1]], _[2]] for _ in vv2_sorted]

    Ostab_named = [[genenames[_], Ostab[_]] for _ in np.argsort(Ostab)]

    return Ostab_named, vv2_named
