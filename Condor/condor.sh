#!/bin/bash

echo "Starting job on " `date` #Date/time of start of job
echo "Running on: `uname -a`" #Condor job is running on this node
source /cvmfs/cms.cern.ch/cmsset_default.sh  ## if a tcsh script, use .csh instead of .sh
#export SCRAM_ARCH=slc6_amd64_gcc630
echo $SCRAM_ARCH
eval `scramv1 project CMSSW CMSSW_9_4_6_patch1`
cd CMSSW_9_4_6_patch1/src
eval `scramv1 runtime -sh`
cd ${_CONDOR_SCRATCH_DIR}
tar -xvf FileList.tar
pwd

cmsRun step1_DIGIPREMIX_S2_DATAMIX_L1_DIGI2RAW_HLT.py $1
cmsRun step2_RAW2DIGI_RECO_RECOSIM_EI.py
cmsRun step3_PAT.py

xrdcp mini_test.root root://cmseos.fnal.gov//${2}/miniAOD_${3}.root
