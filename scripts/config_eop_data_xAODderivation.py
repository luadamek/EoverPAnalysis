# E/p analysis for run 2
# Joakim Olsson (joakim.olsson@cern.ch)

from xAH_config import xAH_config
c = xAH_config()

# input containers
trks = "InDetTrackParticles"

# selected version
trks_loose = trks+"LoosePrimary"
trks_loose_notrt = trks+"LoosePrimaryNoTRT"
trks_tight = trks+"TightPrimary"
trks_run1 = trks+"Run1"

''' Set up all the algorithms '''
c.setalg("BasicEventSelection", {"m_name": "BasicEventSelection",
                                 "m_applyGRLCut": True,
                                 "m_GRLxml": "$ROOTCOREBIN/data/EoverP/data15_13TeV.periodB1_DetStatus-v62-pro18_DQDefects-00-01-02_PHYS_StandardModel_MinimuBias2010.xml",
                                 "m_doPUreweighting": False,
                                 "m_applyPrimaryVertexCut": True,
                                 "m_PVNTrack": 4,
                                 "m_applyEventCleaningCut": True,
                                 "m_applyCoreFlagsCut": True,
                                 "m_applyTriggerCut": True,
                                 "m_triggerSelection": "HLT_noalg_mb_L1MBTS_1",
                                 "m_useMetaData": False,
                                 "m_checkDuplicatesData": False,
                                 "m_checkDuplicatesMC": False})

''' Fill histograms with tracking details, passing only basic event selection'''
c.setalg("TrackHistsAlgo", {"m_name": "Tracks_BasicEvtSel",
                            "m_inContainerName": trks,
                            "m_detailStr": "2D IPDetails HitCounts Chi2Details",
                            "m_debug": False})

''' Select tracks passing the "LoosePrimary" Tracking CP Recommendations (Moriond 2016)'''
# https://twiki.cern.ch/twiki/bin/view/AtlasProtected/TrackingCPMoriond2016
c.setalg("TrackVertexSelection", {"m_name": "TrackSel_LoosePrimary",
                                   "m_inContainerName": trks,
                                   "m_decorateSelectedObjects": False,
                                   "m_createSelectedContainer": True,
                                   "m_pass_min": 1.0,
                                   "m_cutLevel": "LoosePrimary",
                                   "m_maxD0": 2.0,
                                   "m_maxZ0SinTheta": 3.0,
                                   "m_minNTrtHits": 20,
                                   "m_outContainerName": trks_loose,
                                   "m_useCutFlow": False,
                                   "m_debug": False})

''' Fill histograms with tracking details, after LoosePrimary selection '''
c.setalg("TrackHistsAlgo", {"m_name": "Tracks_LoosePrimary",
                            "m_inContainerName": trks_loose,
                            "m_detailStr": "2D IPDetails HitCounts Chi2Details",
                            "m_debug": False})

''' Select tracks passing the "LoosePrimary" but with *NO TRT cut* Tracking CP Recommendations (Moriond 2016)'''
# https://twiki.cern.ch/twiki/bin/view/AtlasProtected/TrackingCPMoriond2016
c.setalg("TrackVertexSelection", {"m_name": "TrackSel_LoosePrimaryNoTRT",
                                   "m_inContainerName": trks,
                                   "m_decorateSelectedObjects": False,
                                   "m_createSelectedContainer": True,
                                   "m_pass_min": 1.0,
                                   "m_cutLevel": "LoosePrimary",
                                   "m_maxD0": 2.0,
                                   "m_maxZ0SinTheta": 3.0,
                                   "m_minNTrtHits": -1,
                                   "m_outContainerName": trks_loose_notrt,
                                   "m_useCutFlow": False,
                                   "m_debug": False})

''' Fill histograms with tracking details, after LoosePrimary but with *NO TRT cut* selection '''
c.setalg("TrackHistsAlgo", {"m_name": "Tracks_LoosePrimaryNoTRT",
                            "m_inContainerName": trks_loose_notrt,
                            "m_detailStr": "2D IPDetails HitCounts Chi2Details",
                            "m_debug": False})

''' Select tracks passing the "TightPrimary" Tracking CP Recommendations (Moriond 2016)'''
# https://twiki.cern.ch/twiki/bin/view/AtlasProtected/TrackingCPMoriond2016
c.setalg("TrackVertexSelection", {"m_name": "TrackSel_TightPrimary",
                                   "m_inContainerName": trks,
                                   "m_decorateSelectedObjects": False,
                                   "m_createSelectedContainer": True,
                                   "m_pass_min": 1.0,
                                   "m_cutLevel": "TightPrimary",
                                   "m_maxD0": 2.0,
                                   "m_maxZ0SinTheta": 3.0,
                                   "m_minNTrtHits": 20,
                                   "m_outContainerName": trks_tight,
                                   "m_useCutFlow": False,
                                   "m_debug": False})

''' Fill histograms with tracking details, after TightPrimary selection '''
c.setalg("TrackHistsAlgo", {"m_name": "Tracks_TightPrimary",
                            "m_inContainerName": trks_tight,
                            "m_detailStr": "2D IPDetails HitCounts Chi2Details",
                            "m_debug": False})

''' Tracks with the same selections as in the ATLAS Run 1 paper '''
# https://cds.cern.ch/record/2006570
c.setalg("TrackVertexSelection", {"m_name": "TrackSel_Run1",
                                   "m_inContainerName": trks,
                                   "m_decorateSelectedObjects": False,
                                   "m_createSelectedContainer": True,
                                   "m_pass_min": 1.0,
                                   "m_cutLevel": "NoCut",
                                   "m_minPt": 500,
                                   "m_maxAbsEta": 2.3,
                                   "m_maxD0": 1.5,
                                   "m_maxZ0SinTheta": 1.5,
                                   "m_minNPixelHits": 1,
                                   "m_minNSctHits": 6,
                                   "m_minNTrtHits": 20,
                                   "m_outContainerName": trks_run1,
                                   "m_useCutFlow": False,
                                   "m_debug": False})

''' Fill histograms with tracking details, after Run1 selection '''
c.setalg("TrackHistsAlgo", {"m_name": "Tracks_Run1",
                            "m_inContainerName": trks_run1,
                            "m_detailStr": "2D IPDetails HitCounts Chi2Details",
                            "m_debug": False})

''' E/p histograms with basic track selection'''
c.setalg("EoverPAnalysis_eopxAOD", {"m_name": "EoverP_BasicEvtSel",
                                    "m_inTrackContainerName": trks,
                                    "m_trkExtrapol": "EMB2",
                                    "m_doBgSubtr" : True,
                                    "m_doEMcalib": True,
                                    "m_doLCWcalib": True,
                                    "m_doCells": True,
                                    "m_doCaloEM": True,
                                    "m_doCaloHAD": True,
                                    "m_doCaloTotal": True,
                                    "m_trkIsoDRmax": .4,
                                    "m_doTrkPcut": True,
                                    "m_trkPmin": 0.,
                                    "m_trkPmax": 1e8,
                                    "m_doTrkEtacut": True,
                                    "m_trkEtamin": 0.,
                                    "m_trkEtamax": 1e8,
                                    "m_doTileCuts": True,
                                    "m_LarEmax": 1e8,
                                    "m_TileEfrac": -1,
                                    "m_doEtaPranges": True,
                                    "m_Ebins": "50, 0., 2.5",
                                    "m_doEbinsArray": True,
                                    "m_EbinsArray": "0.5, 0.8, 1.2, 1.8, 2.2, 2.8, 3.6, 4.6, 5.8, 7.3, 9.2, 11.7, 14.8, 18.7, 23.7, 30",
                                    "m_EtaAbsbins": "50, 0., 2.5",
                                    "m_doEtaAbsbinsArray": True,
                                    "m_EtaAbsbinsArray": "0., .6, 1.1, 1.4, 1.5, 1.8, 1.9, 2.3",
                                    "m_detailStr": "all",
                                    "m_debug": False})

''' E/p histograms with LoosePrimary track selection'''
c.setalg("EoverPAnalysis_eopxAOD", {"m_name": "EoverP_LoosePrimaryTrks",
                                    "m_inTrackContainerName": trks_loose,
                                    "m_trkExtrapol": "EMB2",
                                    "m_doBgSubtr" : True,
                                    "m_doEMcalib": True,
                                    "m_doLCWcalib": True,
                                    "m_doCells": True,
                                    "m_doCaloEM": True,
                                    "m_doCaloHAD": True,
                                    "m_doCaloTotal": True,
                                    "m_trkIsoDRmax": .4,
                                    "m_doTrkPcut": True,
                                    "m_trkPmin": 0.,
                                    "m_trkPmax": 1e8,
                                    "m_doTrkEtacut": True,
                                    "m_trkEtamin": 0.,
                                    "m_trkEtamax": 1e8,
                                    "m_doTileCuts": True,
                                    "m_LarEmax": 1e8,
                                    "m_TileEfrac": -1,
                                    "m_doEtaPranges": True,
                                    "m_Ebins": "50, 0., 2.5",
                                    "m_doEbinsArray": True,
                                    "m_EbinsArray": "0.5, 0.8, 1.2, 1.8, 2.2, 2.8, 3.6, 4.6, 5.8, 7.3, 9.2, 11.7, 14.8, 18.7, 23.7, 30",
                                    "m_EtaAbsbins": "50, 0., 2.5",
                                    "m_doEtaAbsbinsArray": True,
                                    "m_EtaAbsbinsArray": "0., .6, 1.1, 1.4, 1.5, 1.8, 1.9, 2.3",
                                    "m_detailStr": "all",
                                    "m_debug": False})

''' E/p histograms with LoosePrimary but with *NO TRT cut* track selection'''
c.setalg("EoverPAnalysis_eopxAOD", {"m_name": "EoverP_LoosePrimaryTrksNoTRT",
                                    "m_inTrackContainerName": trks_loose_notrt,
                                    "m_trkExtrapol": "EMB2",
                                    "m_doBgSubtr" : True,
                                    "m_doEMcalib": True,
                                    "m_doLCWcalib": True,
                                    "m_doCells": True,
                                    "m_doCaloEM": True,
                                    "m_doCaloHAD": True,
                                    "m_doCaloTotal": True,
                                    "m_trkIsoDRmax": .4,
                                    "m_doTrkPcut": True,
                                    "m_trkPmin": 0.,
                                    "m_trkPmax": 1e8,
                                    "m_doTrkEtacut": True,
                                    "m_trkEtamin": 0.,
                                    "m_trkEtamax": 1e8,
                                    "m_doTileCuts": True,
                                    "m_LarEmax": 1e8,
                                    "m_TileEfrac": -1,
                                    "m_doEtaPranges": True,
                                    "m_Ebins": "50, 0., 2.5",
                                    "m_doEbinsArray": True,
                                    "m_EbinsArray": "0.5, 0.8, 1.2, 1.8, 2.2, 2.8, 3.6, 4.6, 5.8, 7.3, 9.2, 11.7, 14.8, 18.7, 23.7, 30",
                                    "m_EtaAbsbins": "50, 0., 2.5",
                                    "m_doEtaAbsbinsArray": True,
                                    "m_EtaAbsbinsArray": "0., .6, 1.1, 1.4, 1.5, 1.8, 1.9, 2.3",
                                    "m_detailStr": "all",
                                    "m_debug": False})

''' E/p histograms with TightPrimary track selection'''
c.setalg("EoverPAnalysis_eopxAOD", {"m_name": "EoverP_TightPrimaryTrks",
                                    "m_inTrackContainerName": trks_tight,
                                    "m_trkExtrapol": "EMB2",
                                    "m_doBgSubtr" : True,
                                    "m_doEMcalib": True,
                                    "m_doLCWcalib": True,
                                    "m_doCells": True,
                                    "m_doCaloEM": True,
                                    "m_doCaloHAD": True,
                                    "m_doCaloTotal": True,
                                    "m_trkIsoDRmax": .4,
                                    "m_doTrkPcut": True,
                                    "m_trkPmin": 0.,
                                    "m_trkPmax": 1e8,
                                    "m_doTrkEtacut": True,
                                    "m_trkEtamin": 0.,
                                    "m_trkEtamax": 1e8,
                                    "m_doTileCuts": True,
                                    "m_LarEmax": 1e8,
                                    "m_TileEfrac": -1,
                                    "m_doEtaPranges": True,
                                    "m_Ebins": "50, 0., 2.5",
                                    "m_doEbinsArray": True,
                                    "m_EbinsArray": "0.5, 0.8, 1.2, 1.8, 2.2, 2.8, 3.6, 4.6, 5.8, 7.3, 9.2, 11.7, 14.8, 18.7, 23.7, 30",
                                    "m_EtaAbsbins": "50, 0., 2.5",
                                    "m_doEtaAbsbinsArray": True,
                                    "m_EtaAbsbinsArray": "0., .6, 1.1, 1.4, 1.5, 1.8, 1.9, 2.3",
                                    "m_detailStr": "all",
                                    "m_debug": False})

''' E/p histograms with Run 1 track selection'''
c.setalg("EoverPAnalysis_eopxAOD", {"m_name": "EoverP_Run1Trks",
                                    "m_inTrackContainerName": trks_run1,
                                    "m_trkExtrapol": "EMB2",
                                    "m_doBgSubtr" : True,
                                    "m_doEMcalib": True,
                                    "m_doLCWcalib": True,
                                    "m_doCells": True,
                                    "m_doCaloEM": True,
                                    "m_doCaloHAD": True,
                                    "m_doCaloTotal": True,
                                    "m_trkIsoDRmax": .4,
                                    "m_doTrkPcut": True,
                                    "m_trkPmin": 0.,
                                    "m_trkPmax": 1e8,
                                    "m_doTrkEtacut": True,
                                    "m_trkEtamin": 0.,
                                    "m_trkEtamax": 1e8,
                                    "m_doTileCuts": True,
                                    "m_LarEmax": 1e8,
                                    "m_TileEfrac": -1,
                                    "m_doEtaPranges": True,
                                    "m_Ebins": "50, 0., 2.5",
                                    "m_doEbinsArray": True,
                                    "m_EbinsArray": "0.5, 0.8, 1.2, 1.8, 2.2, 2.8, 3.6, 4.6, 5.8, 7.3, 9.2, 11.7, 14.8, 18.7, 23.7, 30",
                                    "m_EtaAbsbins": "50, 0., 2.5",
                                    "m_doEtaAbsbinsArray": True,
                                    "m_EtaAbsbinsArray": "0., .6, 1.1, 1.4, 1.5, 1.8, 1.9, 2.3",
                                    "m_detailStr": "all",
                                    "m_debug": False})

