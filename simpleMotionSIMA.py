import sima
import sima.motion
from sima.motion import HiddenMarkov2D
from shutil import copy, copytree
import argparse
import sys
import os,glob
import shutil

def motion(datadir,app,X,Y,O):
	if O is not None:
		datapath=os.getcwd()
		for root,dirs,files in os.walk(datapath):
			for f in dirs:
				if f.endswith('.sima'):
					shutil.rmtree(root+'/'+f)

	sequences = [sima.Sequence.create('TIFF', datadir)]


	if(app=='2D' or app is None):	
		mc_approach = sima.motion.PlaneTranslation2D(max_displacement=[X, Y])
#	mc_approach=sima.motion.HiddenMarkov2D(granularity='row',max_displacement=[X,Y],verbose=False)
	else:
		 mc_approach=sima.motion.HiddenMarkov2D(granularity='row',max_displacement=[X,Y],verbose=False)
	dataset = mc_approach.correct(sequences, 'HMM_model.sima')
	dataset.export_frames([[['frames.tif']]], fmt='TIFF16')
	



def main(argv):
	argParser=argparse.ArgumentParser()
	argParser.add_argument('-d',"--signalFile", action="store", type=str, default='',
 	   help="the signal pickle file to plot")
	argParser.add_argument('-x','--Xdisp',action="store",type=int,default=10,help='-x disp')
	argParser.add_argument('-y','--Ydisp',action="store",type=int,default=10,help='-y disp')
	argParser.add_argument('-o','--over',action="store",type=str,default=None,help='-o for overwrite')


	argParser.add_argument('-m',"--method", action="store", type=str, default=None,help='MC method')
	args = argParser.parse_args()
	
	motion(args.signalFile,args.method,args.Xdisp,args.Ydisp,args.over)






if __name__=="__main__":
        main(sys.argv[1:])
