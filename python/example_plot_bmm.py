# -*- coding: utf-8 -*-
"""
Created on Mon Apr  19 10:00:00 2020

@author: mccikpc2
"""
import getpass
import matplotlib
matplotlib.use('agg')

from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt

username=getpass.getuser()

#from runsDefine import outputDir
outputDir='/tmp'
fileName=outputDir + '/' + username + '/output1.nc'

def plot_model_run(fileName='/tmp/output1.nc'):
    
    nc=Dataset(fileName)
    
    time=       nc['time'][:]
    z=          nc['z'][:]
    p=          nc['p'][:]
    t=          nc['t'][:]
    rh=         nc['rh'][:]
    w=          nc['w'][:]
    ql=         nc['ql'][:]
    beta_ext=   nc['beta_ext'][:]
    ndrop=      nc['ndrop'][:]
    deff=       nc['deff'][:]
    mwat=       nc['mwat'][:,:,:]
    qi=         nc['qi'][:]
    nice=       nc['nice'][:]
    mice=       nc['mice'][:,:,:]
    

    from mpl_toolkits.axes_grid1 import host_subplot
    import mpl_toolkits.axisartist as AA
    import matplotlib.pyplot as plt
    
    fig = plt.figure(figsize=(15,10))
    
    
    ##########################################################################
    # First plot
    ##########################################################################
    host = host_subplot(221, axes_class=AA.Axes)
    #plt.subplots_adjust(right=0.75)
    
    par1 = host.twinx()
    par2 = host.twinx()
   
    offset = 20
    new_fixed_axis = par1.get_grid_helper().new_fixed_axis
    par1.axis["right"] = new_fixed_axis(loc="right", axes=par1,
                                            offset=(offset, 0))

    par1.axis["right"].toggle(all=True)

   
    offset = 80
    new_fixed_axis = par2.get_grid_helper().new_fixed_axis
    par2.axis["right"] = new_fixed_axis(loc="right", axes=par2,
                                            offset=(offset, 0))
    
    par2.axis["right"].toggle(all=True)
    
    

    host.set_xlabel("Time (s)")
    host.set_ylabel("Mixing ratios (g kg$^{-1}$)")
    par1.set_ylabel("Ice")
    par2.set_ylabel("Humidity")
    
    p1, = host.plot(time, ql*1000., label="cloud")
    p2, = par1.plot(time, qi*1000., label="ice")
    p3, = par2.plot(time, rh, label="humidity")
    
    
    host.legend(loc=6)
    
    host.axis["left"].label.set_color(p1.get_color())
    par1.axis["right"].label.set_color(p2.get_color())
    par2.axis["right"].label.set_color(p3.get_color())
    ##########################################################################

    ##########################################################################
    # Second plot
    ##########################################################################
    host = host_subplot(222, axes_class=AA.Axes)
    # plt.subplots_adjust(right=0.75)
    
    par2 = host.twinx()
    
    offset = 20
    new_fixed_axis = par2.get_grid_helper().new_fixed_axis
    par2.axis["right"] = new_fixed_axis(loc="right", axes=par2,
                                            offset=(offset, 0))
    
    par2.axis["right"].toggle(all=True)
    
    
    host.set_xlabel("Time (s)")
    host.set_ylabel("Pressure (hPa)")
    par2.set_ylabel("T ($^\circ$C)")
    
    p1, = host.plot(time, p/100., label="pressure")
    p3, = par2.plot(time, t-273.15, label="temperature")
    host.invert_yaxis()
    
    host.legend(loc=8)
    
    host.axis["left"].label.set_color(p1.get_color())
    par2.axis["right"].label.set_color(p3.get_color())
    ##########################################################################

    ##########################################################################
    # Third plot
    ##########################################################################
    host = host_subplot(223, axes_class=AA.Axes)
    # plt.subplots_adjust(right=0.75)
    
    par2 = host.twinx()
    
    offset = 20
    new_fixed_axis = par2.get_grid_helper().new_fixed_axis
    par2.axis["right"] = new_fixed_axis(loc="right", axes=par2,
                                            offset=(offset, 0))
    
    par2.axis["right"].toggle(all=True)
    
    
    host.set_xlabel("Time (s)")
    host.set_ylabel("CDNC (cm$^{-3}$)")
    par2.set_ylabel("N$_{ice}$ (L$^{-1}$)")
    
    p1, = host.plot(time, ndrop/1.e6, label="CDNC")
    p3, = par2.plot(time, nice/1.e3, label="N$_{ice}$")
    
    host.legend(loc=6)
    
    host.axis["left"].label.set_color(p1.get_color())
    par2.axis["right"].label.set_color(p3.get_color())
    ##########################################################################

    ##########################################################################
    # Fourth plot
    ##########################################################################
    host = host_subplot(224, axes_class=AA.Axes)
    # plt.subplots_adjust(right=0.75)
    
    
    
    
    host.set_xlabel("Time (s)")
    host.set_ylabel("Drop mass (kg)")
    
    p1=host.plot(time, mwat.reshape((mwat.shape[0],-1)), label="Drop masses")
    
    for i in range(len(p1)):
        if i == 0:
            col=p1[i].get_color()
        p1[i].set_color(col)
        host.axis["left"].label.set_color(col)
    ##########################################################################
    host.set_yscale('log')

    plt.subplots_adjust(wspace=0.8)
   
    plt.ion()
    plt.draw()
    plt.show()
    
    
    
    plt.savefig("/tmp/" + username + "/timeseries.png")

    
    
    nc.close()
    
if __name__=="__main__":
    plot_model_run(fileName)
