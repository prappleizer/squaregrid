import matplotlib.pyplot as plt 

class SquareGrid():
    def __init__(self,fig_width=8):
        self.fig_width = fig_width    
    
    def set_suptitle(self,suptitle,fontsize=16):
        self.fig.set_size_inches(self.figsize[0],self.figsize[1]*1.1)
        self.fig.suptitle(suptitle,fontsize=fontsize)
        return self.fig
    
    def remove_suptitle(self):
        self.fig.suptitle('',fontsize=1)
        return self.fig
    
    def TriGrid(self,primary='right',hidelabels=True,show_indices=False):
        if (primary=='right') or (primary=='left'):
            self.fig_height = self.fig_width / 1.5
        else:
            self.fig_height = self.fig_width *1.5
        self.fig = plt.figure(constrained_layout=True,figsize=(self.fig_width,self.fig_height))
        self.figsize=self.fig.get_size_inches()
        gs = plt.GridSpec(4, 4, figure=self.fig)
        if primary=='left':
            gs = plt.GridSpec(4, 4, figure=self.fig)
            ax1 = self.fig.add_subplot(gs[:, :2])
            ax2 = self.fig.add_subplot(gs[:2,3])
            ax3 = self.fig.add_subplot(gs[2:,3])
            ax =  [ax1,ax2,ax3]
            self.axes = ax
        elif primary=='right':
            gs = plt.GridSpec(4, 4, figure=self.fig)
            ax1 = self.fig.add_subplot(gs[:, 2:])
            ax2 = self.fig.add_subplot(gs[:2,0])
            ax3 = self.fig.add_subplot(gs[2:,0])
            ax =  [ax1,ax2,ax3]
            self.axes = ax
        elif primary=='bottom':
            gs = plt.GridSpec(6,4, figure=self.fig)
            ax1 = self.fig.add_subplot(gs[2:,:])
            ax2 = self.fig.add_subplot(gs[0:2,:2])
            ax3 = self.fig.add_subplot(gs[0:2,2:])
            ax =  [ax1,ax2,ax3]
            self.axes = ax
        elif primary=='top':
            gs = plt.GridSpec(6,4, figure=self.fig)
            ax1 = self.fig.add_subplot(gs[:4,:])
            ax2 = self.fig.add_subplot(gs[4:,:2])
            ax3 = self.fig.add_subplot(gs[4:,2:])
            ax =  [ax1,ax2,ax3]
            self.axes = ax
            
        for i in self.axes:
            i.tick_params(which='both',direction='in',length=6,width=0.8,top=True,right=True)
        if hidelabels:
            for i in self.axes:
                i.tick_params(labelbottom=False,labelleft=False)
        if show_indices:
            for n,i in enumerate(self.axes):
                i.text(0.5,0.5,'{}'.format(n),ha='center',transform=ax[n].transAxes)
        return self.fig, self.axes
    
    
    def QuadGrid(self,primary='left',hidelabels=True,show_indices=False):
        if (primary=='right') or (primary=='left'):
            self.fig_height = self.fig_width / 1.3
        else:
            self.fig_height = self.fig_width * 1.3
        self.fig = plt.figure(constrained_layout=True,figsize=(self.fig_width,self.fig_height))
        self.figsize=self.fig.get_size_inches()

        if primary=='left':
            gs = plt.GridSpec(3, 4, figure=self.fig)
            ax1 = self.fig.add_subplot(gs[:, :3])
            ax2 = self.fig.add_subplot(gs[0,3])
            ax3 = self.fig.add_subplot(gs[1,3])
            ax4 = self.fig.add_subplot(gs[2,3])
            ax =  [ax1,ax2,ax3,ax4]
            self.axes = ax
        elif primary=='right':
            gs = plt.GridSpec(3, 4, figure=self.fig)
            ax1 = self.fig.add_subplot(gs[:, 1:])
            ax2 = self.fig.add_subplot(gs[0,0])
            ax3 = self.fig.add_subplot(gs[1,0])
            ax4 = self.fig.add_subplot(gs[2,0])
            ax =  [ax1,ax2,ax3,ax4]
            self.axes = ax
        elif primary=='bottom':
            gs = plt.GridSpec(4, 3, figure=self.fig)
            ax1 = self.fig.add_subplot(gs[1:,:])
            ax2 = self.fig.add_subplot(gs[0,0])
            ax3 = self.fig.add_subplot(gs[0,1])
            ax4 = self.fig.add_subplot(gs[0,2])
            ax =  [ax1,ax2,ax3,ax4]
            self.axes = ax
        elif primary=='top':
            gs = plt.GridSpec(4, 3, figure=self.fig)
            ax1 = self.fig.add_subplot(gs[0:3,:])
            ax2 = self.fig.add_subplot(gs[3,0])
            ax3 = self.fig.add_subplot(gs[3,1])
            ax4 = self.fig.add_subplot(gs[3,2])
            ax =  [ax1,ax2,ax3,ax4]
            self.axes = ax
        for i in self.axes:
            i.tick_params(which='both',direction='in',length=6,width=0.8,top=True,right=True)
        if hidelabels:
            for i in self.axes:
                i.tick_params(labelbottom=False,labelleft=False)
        if show_indices:
            for n,i in enumerate(self.axes):
                i.text(0.5,0.5,'{}'.format(n),ha='center',transform=ax[n].transAxes)
        return self.fig, self.axes
    
    
    def QuintGrid(self,primary='middle',hidelabels=True,show_indices=False):
        self.fig_height = self.fig_width / 1.9
        self.fig = plt.figure(constrained_layout=True,figsize=(self.fig_width,self.fig_height))
        self.figsize=self.fig.get_size_inches()
        gs = plt.GridSpec(4, 9, figure=self.fig)
        if primary=='middle':
            ax1 = self.fig.add_subplot(gs[:, 2:6])
            ax2 = self.fig.add_subplot(gs[:2,0:2])
            ax3 = self.fig.add_subplot(gs[2:,0:2])
            ax4 = self.fig.add_subplot(gs[:2,-2:])
            ax5 = self.fig.add_subplot(gs[2:,-2:])
        elif primary=='left':
            ax1 = self.fig.add_subplot(gs[:, 0:4])
            ax2 = self.fig.add_subplot(gs[:2,4:6])
            ax3 = self.fig.add_subplot(gs[:2,-2:])
            ax4 = self.fig.add_subplot(gs[2:,4:6])
            ax5 = self.fig.add_subplot(gs[2:,-2:])
        
        elif primary=='right':
            ax1 = self.fig.add_subplot(gs[:, 5:])
            ax2 = self.fig.add_subplot(gs[:2,0:2])
            ax3 = self.fig.add_subplot(gs[:2,3:5])
            ax4 = self.fig.add_subplot(gs[2:,0:2])
            ax5 = self.fig.add_subplot(gs[2:,3:5])
        
        ax =  [ax1,ax2,ax3,ax4,ax5]
        self.axes = ax
        for i in self.axes:
            i.tick_params(which='both',direction='in',length=6,width=0.8,top=True,right=True)
        if hidelabels:
            for i in self.axes:
                i.tick_params(labelbottom=False,labelleft=False)
        if show_indices:
            for n,i in enumerate(self.axes):
                i.text(0.5,0.5,'{}'.format(n),ha='center',transform=ax[n].transAxes)
        return self.fig, self.axes
    
    def LGrid(self,pos='upper_right',hidelabels=True,show_indices=False):
        self.fig_height = self.fig_width * 1
        self.fig = plt.figure(constrained_layout=True,figsize=(self.fig_width,self.fig_height))
        self.figsize=self.fig.get_size_inches()    
        gs = plt.GridSpec(6,6, figure=self.fig)
        if (pos == 'upper_right') or (pos == 'ur'):
            ax1 = self.fig.add_subplot(gs[0:4,2:])
            ax2 = self.fig.add_subplot(gs[0:2,0:2])
            ax3 = self.fig.add_subplot(gs[2:4,0:2])
            ax4 = self.fig.add_subplot(gs[4:6,0:2])
            ax5 = self.fig.add_subplot(gs[4:6,2:4])
            ax6 = self.fig.add_subplot(gs[4:6,4:6])
            ax =  [ax1,ax2,ax3,ax4,ax5,ax6]
            self.axes = ax
        elif (pos == 'upper_left') or (pos == 'ul'):
            ax1 = self.fig.add_subplot(gs[0:4,0:4])
            ax2 = self.fig.add_subplot(gs[4:6,0:2])
            ax3 = self.fig.add_subplot(gs[4:6,2:4])
            ax4 = self.fig.add_subplot(gs[4:6,4:6])
            ax5 = self.fig.add_subplot(gs[2:4,4:])
            ax6 = self.fig.add_subplot(gs[0:2,4:])
            ax =  [ax1,ax2,ax3,ax4,ax5,ax6]
            self.axes = ax
        elif (pos == 'lower_left') or (pos == 'll'):
            ax1 = self.fig.add_subplot(gs[2:,0:4])
            ax2 = self.fig.add_subplot(gs[0:2,0:2])
            ax3 = self.fig.add_subplot(gs[0:2,2:4])
            ax4 = self.fig.add_subplot(gs[0:2,4:])
            ax5 = self.fig.add_subplot(gs[2:4,4:])
            ax6 = self.fig.add_subplot(gs[4:6,4:6])
            ax =  [ax1,ax2,ax3,ax4,ax5,ax6]
            self.axes = ax
        elif (pos == 'lower_right') or (pos=='lr'):
            ax1 = self.fig.add_subplot(gs[2:,2:])
            ax2 = self.fig.add_subplot(gs[4:6,0:2])
            ax3 = self.fig.add_subplot(gs[2:4,0:2])
            ax4 = self.fig.add_subplot(gs[0:2,0:2])
            ax5 = self.fig.add_subplot(gs[0:2,2:4])
            ax6 = self.fig.add_subplot(gs[0:2,4:])
            ax =  [ax1,ax2,ax3,ax4,ax5,ax6]
            self.axes = ax
        for i in self.axes:
            i.tick_params(which='both',direction='in',length=6,width=0.8,top=True,right=True)
        if hidelabels:
            for i in self.axes:
                i.tick_params(labelbottom=False,labelleft=False)
        if show_indices:
            for n,i in enumerate(self.axes):
                i.text(0.5,0.5,'{}'.format(n),ha='center',transform=ax[n].transAxes)
        return self.fig, self.axes
    
    def UGrid(self,orientation='up',hidelabels=True,show_indices=False):
        self.fig_height = self.fig_width /1.5
        self.fig = plt.figure(constrained_layout=True,figsize=(self.fig_width,self.fig_height))
        self.figsize=self.fig.get_size_inches()    
        gs = plt.GridSpec(6,9, figure=self.fig)
        if (orientation == 'down'):
            ax1 = self.fig.add_subplot(gs[2:6,2:6])
            ax2 = self.fig.add_subplot(gs[4:6,0:2])
            ax6 = self.fig.add_subplot(gs[0:2,4:6])
            ax3 = self.fig.add_subplot(gs[2:4,0:2])
            ax4 = self.fig.add_subplot(gs[0:2,0:2])
            ax5 = self.fig.add_subplot(gs[0:2,2:4])
            
            ax7 = self.fig.add_subplot(gs[0:2,6:8])
            ax8 = self.fig.add_subplot(gs[2:4,6:8])
            ax9 = self.fig.add_subplot(gs[4:6,6:8])
            ax =  [ax1,ax2,ax3,ax4,ax5,ax6,ax7,ax8,ax9]
            self.axes = ax
        elif orientation =='up':
            ax1 = self.fig.add_subplot(gs[0:4,2:6])
            ax2 = self.fig.add_subplot(gs[0:2,0:2])
            ax3 = self.fig.add_subplot(gs[2:4,0:2])
            ax4 = self.fig.add_subplot(gs[4:6,0:2])
            ax5 = self.fig.add_subplot(gs[4:6,2:4])
            ax6 = self.fig.add_subplot(gs[4:6,4:6])
            ax7 = self.fig.add_subplot(gs[4:6,6:8])
            ax8 = self.fig.add_subplot(gs[2:4,6:8])
            ax9 = self.fig.add_subplot(gs[0:2,6:8])
            ax =  [ax1,ax2,ax3,ax4,ax5,ax6,ax7,ax8,ax9]
            self.axes = ax
        for n,i in enumerate(self.axes):
            i.tick_params(which='both',direction='in',length=6,width=0.8,top=True,right=True)
            
        if hidelabels:
            for i in self.axes:
                i.tick_params(labelbottom=False,labelleft=False)
        if show_indices:
            for n,i in enumerate(self.axes):
                i.text(0.5,0.5,'{}'.format(n),ha='center',transform=ax[n].transAxes)
        return self.fig, self.axes