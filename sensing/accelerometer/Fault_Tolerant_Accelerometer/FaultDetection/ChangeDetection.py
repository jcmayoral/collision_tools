# Author: Tony DiCola
# Modified: Jose Carlos Mayoral
# License: Public Domain
import time
import matplotlib
matplotlib.use('Agg')
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from datetime import datetime
import Adafruit_ADXL345
import numpy as np

class ChangeDetection:

    def __init__(self, seconds):
        #print("MathAccelerometer Constructor")
        self.accel = Adafruit_ADXL345.ADXL345()
        self.seconds = seconds
        self.cum_sum = np.array([0,0,0])
        #self.fig = plt.figure()

    def mean(self,data):
        return np.mean(data, axis=0)

    def variance(self,data):
        return np.var(data, axis=0)

    def plot(self):
        while True:
            samples = []
            for i in range(0,500):
                samples.append(self.accel.read())
            mean = self.mean(samples)
            variance = self.variance(samples)
            #print('Mean Values X={0}, Y={1}, Z={2}'.format(mean[0], mean[1], mean[2]))
            #print('Variance Values X={0}, Y={1}, Z={2}'.format(variance[0], variance[1], variance[2]))

    def changeDetection(self):
        #print ('time in seconds ', self.seconds)
        expected_mean = np.array([2,2,250])
        expected_variance = np.array([1,1,1])
        samples = []
        z_i = self.accel.read()
        samples.append(z_i)
        counter = 0
        ##datetime.date.fromordinal(self.seconds)
        
        while True:

            timeout = time.time() + self.seconds
            while time.time() < timeout:
                return (samples)
	        #print ('remaining ' , timeout - time.time())
            z_i = self.accel.read()
            samples.append(z_i)
            mean = self.mean(samples)
            variance = self.variance(samples)
            self.CUSUM(z_i,mean,variance, expected_mean, expected_variance)
            
                
            #plt.plot([self.cum_sum,np.arange(0,len(self.cum_sum))])
            #plt.show()
            #counter = 0
                

    def CUSUM(self, data, mean, var, e_mean, e_var):
        array = np.array(data)
        s_z = self.meanGaussianSequence(array, mean, var, e_mean)

        if not np.isinf(s_z).any():
            self.cum_sum = np.sum([self.cum_sum,s_z],axis=0)

    def meanGaussianSequence(self,z, m1, v1, m0):
        constants = (m0-m1)/np.power(v1,2)
        m0m1 = (m0+m1)/2
        s_z = constants * (z  - m0m1)
        return s_z