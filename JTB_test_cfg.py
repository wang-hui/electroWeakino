# Import CMS python class definitions such as Process, Source, and EDProducer
import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras
process = cms.Process('jetToolbox', eras.Run2_2017)

process.load("Configuration.EventContent.EventContent_cff")
process.load('Configuration.Geometry.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = '94X_mc2017_realistic_v10'

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10) )

process.source = cms.Source("PoolSource", 
    fileNames = cms.untracked.vstring(
    #"file:mini_test.root"
    "/store/mc/RunIIFall17MiniAODv2/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/910000/D842F996-2149-E811-AF09-0242AC1C0502.root")
    )

process.JTBout = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('mini_JTB_test.root'),
    outputCommands = cms.untracked.vstring("keep *")
    )
process.endpath = cms.EndPath(process.JTBout)

from JMEAnalysis.JetToolbox.jetToolbox_cff import jetToolbox
jetToolbox(process, 'ak12', 'jetSequence', 'JTBout',
            miniAOD=True,
            PUMethod='Puppi', JETCorrPayload='AK8PFPuppi',
            runOnMC=True,
            Cut='pt > 50.0 && abs(eta) < 2.4',
            bTagDiscriminators=['pfBoostedDoubleSecondaryVertexAK8BJetTags'],
            addSoftDrop=True,
            addSoftDropSubjets=True,
            addPruning=True,
            addNsub=True,
            addEnergyCorrFunc=True,
            ) 
