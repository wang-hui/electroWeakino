# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step1 --filein file:root://cmseos.fnal.gov//store/user/sthayil/rpvhiggsinos/gensim/testforhui/GENSIM_2017_NanoAODcompatible_oneproc_mn1_300_mx1_310_0.root --fileout file:raw_test.root --pileup_input file:root://cmseos.fnal.gov//store/user/huiwang/ElectroWeakino/Neutrino_E-10_gun_GEN-SIM-DIGI-RAW_MC_v2_94X_mc2017_realistic_v9-v1_6833D6DC-21CE-E711-ABF0-001E677925E8.root --mc --eventcontent RAWSIM --datatier GEN-SIM-RAW --conditions 94X_mc2017_realistic_v10 --step DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:2e34v40 --datamix PreMix --era Run2_2017 -n 10
import FWCore.ParameterSet.Config as cms
import sys

from Configuration.StandardSequences.Eras import eras

process = cms.Process('HLT',eras.Run2_2017)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.DigiDMPreMix_cff')
process.load('SimGeneral.MixingModule.digi_MixPreMix_cfi')
process.load('Configuration.StandardSequences.DataMixerPreMix_cff')
process.load('Configuration.StandardSequences.SimL1EmulatorDM_cff')
process.load('Configuration.StandardSequences.DigiToRawDM_cff')
process.load('HLTrigger.Configuration.HLT_2e34v40_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

mn1 = sys.argv[2]
mx1 = sys.argv[3]
file_index = sys.argv[4]

# Input source
process.source = cms.Source("PoolSource",
    #fileNames = cms.untracked.vstring('file:root://cmseos.fnal.gov//store/user/sthayil/rpvhiggsinos/gensim/testforhui/GENSIM_2017_NanoAODcompatible_oneproc_mn1_300_mx1_310_0.root'),
    fileNames = cms.untracked.vstring('file:root://cmseos.fnal.gov//store/user/sthayil/rpvhiggsinos/gensim/testforhui/GENSIM_2017_NanoAODcompatible_oneproc_mn1_' + mn1 + '_mx1_' + mx1 + '_' + file_index + '.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step1 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RAW'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    fileName = cms.untracked.string('file:raw_test.root'),
    #fileName = cms.untracked.string('file:raw_' + 'mn1_' + mn1 + '_mx1_' + mx1 + '_' + file_index + '.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.digitizers = cms.PSet(process.theDigitizersMixPreMix)
#process.mixData.input.fileNames = cms.untracked.vstring(['file:root://cmseos.fnal.gov//store/user/huiwang/ElectroWeakino/Neutrino_E-10_gun_GEN-SIM-DIGI-RAW_MC_v2_94X_mc2017_realistic_v9-v1_6833D6DC-21CE-E711-ABF0-001E677925E8.root'])
process.mixData.input.fileNames = cms.untracked.vstring(['file:root://cmseos.fnal.gov//store/user/huiwang/ElectroWeakino/Neutrino_E-10_gun_GEN-SIM-DIGI-RAW_MC_v2_94X_mc2017_realistic_v9-v1_2EA05F08-17CE-E711-8DEC-A4BF0112BC6A.root'])
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '94X_mc2017_realistic_v10', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi)
process.datamixing_step = cms.Path(process.pdatamix)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.datamixing_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.RAWSIMoutput_step])
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC 

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
