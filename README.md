# ElectroWeakino miniAOD producer
This is a git repo to make ntuple from gen-sim to miniAOD
The step of making nanoAOD from miniAOD and coresponding analyzer can be found the this repo
https://github.com/wang-hui/electroWeakino_NanoAOD

1. setup CMSSW. 2017 samples are produced in 94X
```
cmsrel CMSSW_9_4_0_patch1
cd CMSSW_9_4_0_patch1/src
cmsenv
```
2. checkout this repo
```
git clone git@github.com:wang-hui/electroWeakino.git
cd electroWeakino
```
3. local test
```
cmsRun step1_DIGIPREMIX_S2_DATAMIX_L1_DIGI2RAW_HLT.py #add pileup and produce raw
cmsRun step2_RAW2DIGI_RECO_RECOSIM_EI.py #produce AOD
cmsRun step3_PAT.py #produce miniAOD
```
and use the corresponding xx_analysis.py to check the output of each step
4. submit condor
```
cd Condor
python make_condor_cfg.py
condor_submit condor_submit.txt
```
