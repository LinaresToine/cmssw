import FWCore.ParameterSet.Config as cms

hltPhase2L3MuonHighPtTripletStepTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('highPtTripletStep'),
    Fitter = cms.string('FlexibleKFFittingSmoother'),
    GeometricInnerState = cms.bool(False),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("hltMeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    TrajectoryInEvent = cms.bool(False),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("hltPhase2L3MuonHighPtTripletStepTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)
