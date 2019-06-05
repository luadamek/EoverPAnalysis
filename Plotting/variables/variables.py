from calculation.calculation import calculation, calculationDataMC, weightCalculation
import numpy as np
from math import pi

#trk_TotalPhotonBackgroundCalibHitEnergy_EM_200
#trk_TotalHadronicBackgroundCalibHitEnergy_EM_275
#trk_TotalCalibHitEnergy_EM_200

def TruthMomentum(trk):
    return trk["trk_truthP"]
calc_TruthMomentum = calculation(TruthMomentum, ["trk_truthP"])

def TotalCalibHitEnergyEM(trk):
    return trk["trk_TotalPhotonBackgroundCalibHitEnergy_EM_200"] + trk["trk_TotalHadronicBackgroundCalibHitEnergy_EM_200"] + trk["trk_TotalCalibHitEnergy_EM_200"]

def TotalCalibHitEnergyHAD(trk):
    return trk["trk_TotalPhotonBackgroundCalibHitEnergy_HAD_200"] + trk["trk_TotalHadronicBackgroundCalibHitEnergy_HAD_200"] + trk["trk_TotalCalibHitEnergy_HAD_200"]

def TotalCalibHitEnergy(trk):
    return TotalCalibHitEnergyEM(trk) + TotalCalibHitEnergyHAD(trk)

CalibHitBranches = ["trk_TotalPhotonBackgroundCalibHitEnergy_EM_200", "trk_TotalHadronicBackgroundCalibHitEnergy_EM_200", "trk_TotalCalibHitEnergy_EM_200","trk_TotalPhotonBackgroundCalibHitEnergy_HAD_200", "trk_TotalHadronicBackgroundCalibHitEnergy_HAD_200", "trk_TotalCalibHitEnergy_HAD_200"]

def HasCalibHit(trk):
    return TotalCalibHitEnergy(trk) > 0.0
sel_HasCalibHit = calculation(HasCalibHit, CalibHitBranches)

def HasEMCalibHit(trk):
    return TotalCalibHitEnergyEM(trk) > 0.0
sel_HasEMCalibHit = calculation(HasCalibHit, CalibHitBranches)

def HasHADCalibHit(trk):
    return TotalCalibHitEnergyHAD(trk) > 0.0
sel_HasHADCalibHit = calculation(HasHADCalibHit, CalibHitBranches)

def CalibHitFrac(trk):
    return (trk["trk_TotalCalibHitEnergy_EM_200"] + trk["trk_TotalCalibHitEnergy_HAD_200"]) / TotalCalibHitEnergy(trk)
calc_CalibHitFrac = calculation(CalibHitFrac, CalibHitBranches)

def PhotonCalibHitFrac(trk):
    return (trk["trk_TotalPhotonBackgroundCalibHitEnergy_EM_200"] + trk["trk_TotalPhotonBackgroundCalibHitEnergy_HAD_200"]) / TotalCalibHitEnergy(trk)
calc_PhotonCalibHitFrac = calculation(PhotonCalibHitFrac, CalibHitBranches)

def HadronCalibHitFrac(trk):
    return (trk["trk_TotalHadronicBackgroundCalibHitEnergy_EM_200"] + trk["trk_TotalHadronicBackgroundCalibHitEnergy_HAD_200"]) / TotalCalibHitEnergy(trk)
calc_HadronCalibHitFrac = calculation(HadronCalibHitFrac, CalibHitBranches)

def EMCalibHitFrac(trk):
    return (trk["trk_TotalCalibHitEnergy_EM_200"]) / TotalCalibHitEnergyEM(trk)
calc_EMCalibHitFrac = calculation(EMCalibHitFrac, CalibHitBranches)

def HADCalibHitFrac(trk):
    return (trk["trk_TotalCalibHitEnergy_HAD_200"]) / TotalCalibHitEnergyHAD(trk)
calc_HADCalibHitFrac = calculation(HADCalibHitFrac, CalibHitBranches)

def PhotonEMCalibHitFrac(trk):
    return (trk["trk_TotalPhotonBackgroundCalibHitEnergy_EM_200"] ) / TotalCalibHitEnergyEM(trk)
calc_PhotonEMCalibHitFrac = calculation(PhotonEMCalibHitFrac, CalibHitBranches)

def PhotonHADCalibHitFrac(trk):
    return (trk["trk_TotalPhotonBackgroundCalibHitEnergy_HAD_200"] ) / TotalCalibHitEnergyHAD(trk)
calc_PhotonHADCalibHitFrac = calculation(PhotonHADCalibHitFrac, CalibHitBranches)

def HadronCalibHitFrac(trk):
    return (trk["trk_TotalHadronicBackgroundCalibHitEnergy_EM_200"] + trk["trk_TotalHadronicBackgroundCalibHitEnergy_HAD_200"]) / TotalCalibHitEnergy(trk)
calc_HadronCalibHitFrac = calculation(HadronCalibHitFrac, CalibHitBranches)

def HadronEMCalibHitFrac(trk):
    return (trk["trk_TotalHadronicBackgroundCalibHitEnergy_EM_200"] )/ TotalCalibHitEnergyEM(trk)
calc_HadronEMCalibHitFrac = calculation(HadronEMCalibHitFrac, CalibHitBranches)

def HadronHADCalibHitFrac(trk):
    return (trk["trk_TotalHadronicBackgroundCalibHitEnergy_HAD_200"] )/ TotalCalibHitEnergyHAD(trk)
calc_HadronHADCalibHitFrac = calculation(HadronHADCalibHitFrac, CalibHitBranches)

def HadFrac(trk):
    return (trk["trk_ClusterEnergy_HAD_200"]) / (trk["trk_ClusterEnergy_EM_200"] + trk["trk_ClusterEnergy_HAD_200"])
branches = ["trk_ClusterEnergy_EM_200", "trk_ClusterEnergy_HAD_200"]
calc_HadFrac = calculation(HadFrac, branches)

def MomentumHadFrac(trk):
    return (trk["trk_ClusterEnergy_HAD_200"])/trk["trk_p"]
branches = ["trk_ClusterEnergy_HAD_200", "trk_p"]
calc_MomentumHadFrac = calculation(MomentumHadFrac, branches)

def EnergyEMDR100(trk):
    return (trk["trk_ClusterEnergy_EM_100"])
branches = ["trk_ClusterEnergy_EM_100"]
calc_EnergyEMDR100 = calculation(EnergyEMDR100, branches)

def nTRT(trk):
    return trk["trk_nTRT"]
branches = ["trk_nTRT"]
calc_nTRT = calculation(nTRT, branches)

def trkCount(trk):
    return np.zeros(len(trk))
branches = []
calc_trkCount = calculation(trkCount, branches)

def trkNClusters_template(trk, rad1, rad2):
    nclusters_EM = trk["trk_nclusters_EM_" + rad1] - trk["trk_nclusters_EM_" + rad2]
    nclusters_HAD = trk["trk_nclusters_HAD_" + rad1] - trk["trk_nclusters_HAD_" + rad2]
    return nclusters_EM + nclusters_HAD

def trkNClusters(trk):
    return trk["trk_nclusters_EM_200"] + trk["trk_nclusters_HAD_200"]
calc_trkNClusters = calculation(trkNClusters, ["trk_nclusters_EM_200", "trk_nclusters_HAD_200"])

def trkNClusters_EM(trk):
    return trk["trk_nclusters_EM_200"]
calc_trkNClusters_EM = calculation(trkNClusters_EM, ["trk_nclusters_EM_200"])

def trkNClusters_emlike(trk):
    return trk["trk_nclusters_EM_emlike_200"] + trk["trk_nclusters_HAD_emlike_200"]
calc_trkNClusters_emlike = calculation(trkNClusters_emlike, ["trk_nclusters_EM_emlike_200","trk_nclusters_HAD_emlike_200"])

def trkNClusters_HAD(trk):
    return trk["trk_nclusters_HAD_200"]
calc_trkNClusters_HAD = calculation(trkNClusters_HAD, ["trk_nclusters_HAD_200"])

def trkNClusters_hadlike(trk):
    return trk["trk_nclusters_EM_hadlike_200"] + trk["trk_nclusters_HAD_hadlike_200"]
calc_trkNClusters_hadlike = calculation(trkNClusters_hadlike, ["trk_nclusters_EM_hadlike_200", "trk_nclusters_HAD_hadlike_200"])

def trkHADFraction(trk):
    return_value = np.zeros(len(trk))
    return_value = (trk["trk_ClusterEnergy_HAD_200"])/(trk["trk_ClusterEnergy_HAD_200"] + trk["trk_ClusterEnergy_EM_200"])
    return return_value
branches = ["trk_ClusterEnergy_EM_200", "trk_ClusterEnergy_HAD_200"]
calc_trkHADFraction = calculation(trkHADFraction, branches)

def trkEMFraction(trk):
    return_value = np.zeros(len(trk))
    return_value = trk["trk_ClusterEnergy_EM_200"]/(trk["trk_ClusterEnergy_EM_200"] + trk["trk_ClusterEnergy_HAD_200"])
    return return_value
branches = ["trk_ClusterEnergy_EM_200", "trk_ClusterEnergy_HAD_200"]
calc_trkEMFraction = calculation(trkEMFraction, branches)

def trkPt(trk):
    return trk["trk_pt"]
branches = ["trk_pt"]
calc_trkPt = calculation(trkPt, branches)

def trkEtaID(trk):
    return trk["trk_etaID"]
branches = ["trk_etaID"]
calc_trkEta = calculation(trkEtaID, branches)

def trkEtaID_ABS(trk):
    return np.abs(trk["trk_etaID"])
branches = ["trk_etaID"]
calc_trkEta_ABS = calculation(trkEtaID_ABS, branches)

def trkEtaPhiECAL(trk):
    trk_etaEMB = np.abs(trk["trk_etaEMB2"])
    trk_phiEMB = np.abs(trk["trk_phiEMB2"])
    trk_etaEME = np.abs(trk["trk_etaEME2"])
    trk_phiEME = np.abs(trk["trk_phiEME2"])

    has_barrel_extrap = trk_etaEMB < 1000.0
    has_endcap_extrap = trk_etaEME < 1000.0

    has_both = has_barrel_extrap & has_endcap_extrap
    has_one = np.logical_not(has_both) & (has_endcap_extrap | has_barrel_extrap)

    #this will be the eta coordinates used to calculate the acceptance
    trk_eta = np.ones(len(trk)) * 99999999.0
    trk_phi = np.ones(len(trk)) * 99999999.0

    #if there is only one extrapolated coordinate, then it is easy
    trk_eta[has_one & has_barrel_extrap] = trk_etaEMB[has_one & has_barrel_extrap] 
    trk_phi[has_one & has_barrel_extrap] = trk_phiEMB[has_one & has_barrel_extrap] 
    trk_eta[has_one & has_endcap_extrap] = trk_etaEME[has_one & has_endcap_extrap] 
    trk_phi[has_one & has_endcap_extrap] = trk_phiEME[has_one & has_endcap_extrap] 

    #if there are two extrapolated coordinates, take the one in the barrel
    trk_eta[has_both] = trk_etaEMB[has_both]
    trk_phi[has_both] = trk_phiEMB[has_both]

    return trk_eta, trk_phi

def trkEtaECAL(trk):
    return trkEtaPhiECAL(trk)[0]
branches = ["trk_etaEMB2","trk_etaEME2", "trk_phiEMB2", "trk_phiEME2"]
calc_trkEtaECAL = calculation(trkEtaECAL, branches)

def trkPhiECAL(trk):
    return trkEtaPhiECAL(trk)[1]
branches = ["trk_phiEMB2","trk_phiEME2", "trk_etaEMB2","trk_etaEME2"]
calc_trkPhiECAL = calculation(trkPhiECAL, branches)

def trkNearestNeighbourEM2(trk):
    return trk["trk_nearest_dR_EM"]
branches = ["trk_nearest_dR_EM"]
calc_trkNearestNeighbourEM2 =  calculation(trkNearestNeighbourEM2, branches)

def trkNPV2(trk):
    return trk["trk_NPV_2"]
branches = ["trk_NPV_2"]
calc_trkNPV2 = calculation(trkNPV2, branches)

def trkNPV4(trk):
    return trk["trk_NPV_4"]
branches = ["trk_NPV_4"]
calc_trkNPV4 = calculation(trkNPV4, branches)

def trkAverageMu(trk):
    return trk["trk_averagemu"]
branches = ["trk_averagemu"]
calc_trkAverageMu = calculation(trkAverageMu, branches)

def trkP(trk):
    return trk["trk_p"]
branches = ["trk_p"]
calc_trkP = calculation(trkP, branches)

def trkEtaID(trk):
    return trk["trk_etaID"]
branches = ["trk_etaID"]
calc_trkEtaID = calculation(trkEtaID, branches)

def trkEtaEME2(trk):
    return trk["trk_etaEME2"]
branches = ["trk_etaEME2"]
calc_trkEtaEME2 = calculation(trkEtaEME2, branches)

def trkEtaEMB2(trk):
    return trk["trk_etaEMB2"]
branches = ["trk_etaEMB2"]
calc_trkEtaEMB2 = calculation(trkEtaEMB2, branches)

def EnergyAnulus(trk):
    return trk["trk_ClusterEnergy_EM_200"] - trk["trk_ClusterEnergy_EM_100"]
branches = ["trk_ClusterEnergy_EM_200", "trk_ClusterEnergy_EM_100"]
calc_EnergyAnulus = calculation(EnergyAnulus, branches)

def EOPBkg(trk):
    return (1./trk["trk_p"]) * (4.0/3.0) * (EnergyAnulus(trk))
branches = ["trk_ClusterEnergy_EM_200", "trk_ClusterEnergy_EM_100", "trk_p"]
calc_EOPBkg = calculation(EOPBkg, branches)

def EOP(trk):
    return (trk["trk_ClusterEnergy_EM_200"] + trk["trk_ClusterEnergy_HAD_200"])/trk["trk_p"]
branches = ["trk_ClusterEnergy_EM_200", "trk_ClusterEnergy_HAD_200", "trk_p"]
calc_EOP = calculation(EOP, branches)

def DPhi(trk):
    dphi = np.ones(len(trk)) * 100000000.0
    hasEMB2 = np.abs(trk["trk_phiEMB2"]) < 40
    hasEME2 = np.abs(trk["trk_phiEME2"]) < 40

    dphi[hasEME2] = np.abs(trk["trk_phiID"] - trk["trk_phiEME2"])[hasEME2]
    dphi[hasEMB2] = np.abs(trk["trk_phiID"] - trk["trk_phiEMB2"])[hasEMB2]
    greater_than_pi = dphi > pi

    dphi[greater_than_pi] = 2.0 * pi - dphi[greater_than_pi]
    return dphi
branches = ["trk_phiEMB2", "trk_phiEME2","trk_phiID"]
calc_trkDPhi = calculation(DPhi, branches)

def DEta(trk):
    deta = np.ones(len(trk)) * 100000000.0
    hasEMB2 = np.abs(trk["trk_etaEMB2"]) < 40
    hasEME2 = np.abs(trk["trk_etaEME2"]) < 40

    deta[hasEME2] = np.abs(trk["trk_etaID"] - trk["trk_etaEME2"])[hasEME2]
    deta[hasEMB2] = np.abs(trk["trk_etaID"] - trk["trk_etaEMB2"])[hasEMB2]
    return deta

branches = ["trk_etaEMB2", "trk_etaEME2","trk_etaID"]
calc_trkDEta = calculation(DEta, branches)

def weight(trk, isData):
    if not isData:
        return trk["trkWeight"]
    return np.ones(len(trk))
branches = ["trkWeight"]
calc_weight = weightCalculation(weight, branches)