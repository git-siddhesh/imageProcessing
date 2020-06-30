import copy
import numpy as np 
import cv2
int R = 53
int snr = 5200
imgIn = cv2.imread("original.jpg",0)
    // it needs to process even image only
    //Rect roi = Rect(0, 0, imgIn.cols & -2, imgIn.rows & -2);
roi = imgIn[0:(imgIn.shape[0] & -2), 0:(imgIn.shape[1] & -2)]
    //Hw calculation (start)
    //calcPSF(h, roi.shape, R);
outputImg = h,filterSize = roi
     //Mat h(filterSize, CV_32F, Scalar(0));
center = (filterSize.shape[1] / 2, filterSize.shape[0] / 2)
cv2.Circle(h, center, R, color = 255, thickness=1, lineType=8, shift=0)
summa = np.sum(h);
outputImg = h / summa[0];
#-----------------------------------------------------------------------------------------------------
#calcWnrFilter(h, Hw, 1.0 / double(snr));
input_h_PSF = h
output_G = Hw
nsr = 1.0/float(snr)   
#---------------------------------------------------------------
#fftshift(input_h_PSF, h_PSF_shifted);
inputImg = input_h_PSF
outputImg = inputImg;
cx = outputImg.shape[0] / 2
cy = outputImg.shape[1] / 2
q0 = outputImg[0:cx, 0:cy]         # Top-Left - Create a ROI per quadrant
q1 = outputImg[cx:cx+cx, 0:cy]     # Top-Right
q2 = outputImg[0:cx, cy:cy+cy]     # Bottom-Left
q3 = outputImg[cx:cx+cx, cy:cy+cy] # Bottom-Right

tmp = np.copy(q0)               # swap quadrants (Top-Left with Bottom-Right)
outputImg[0:cx, 0:cy] = q3
outputImg[cx:cx + cx, cy:cy + cy] = tmp

tmp = np.copy(q1)               # swap quadrant (Top-Right with Bottom-Left)
outputImg[cx:cx + cx, 0:cy] = q2
outputImg[0:cx, cy:cy + cy] = tmp  
#------------------------------------------------------------------ffshift() 
h_PSF_shifted =outputImg
planes = [np.float32(h_PSF_shifted.copy()), np.zeros(h_PSF_shifted.shape, np.float32)
complexI = cv2.merge(planes)         # Add to the expanded another plane with zeros
cv2.dft(complexI, complexI,DFT_SCALE)         # this way the result may fit in the source matrix
cv2.split(complexI, planes)
cv2.Pow(abs(planes[0]),denom, 2)
denom += nsr
cv2.divide(planes[0], denom, output_G)
    //Hw calculation (stop)
#---------------------------------------------------------------------------------------------------weiner()    
#filtering (start)
#filter2DFreq(imgIn(roi), imgOut, Hw);
inputImg = imgIn(roi), H = Hw
planes = [np.float32(inputImg.copy()), np.zeros(inputImg.shape, np.float32)
complexI = cv.merge(planes)         # Add to the expanded another plane with zeros
cv2.dft(complexI, complexI,DFT_SCALE)         # this way the result may fit in the source matrix

planesH = [np.float32(H.copy()), np.zeros(H.shape, np.float32)
complexH = cv2.merge(planesH)         # Add to the expanded another plane with zeros
cv2.MulSpectrums(complexI, complexH, complexIH, 0) 
cv2.idft(complexIH,complexIH)
cv.split(complexIH, planes)             
outputImg = planes[0];
# filtering (stop)
imgOut = outputImg
# filter2dfreq terminates
imgOut.convertTo(imgOut, CV_8U);
normalize(imgOut, imgOut, 0, 255, NORM_MINMAX);
imwrite("result.jpg", imgOut);
