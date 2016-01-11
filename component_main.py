from kronos.utils import ComponentAbstract
import os


class Component(ComponentAbstract):
    
    """
    generates the following plots using hmm copy:
        - Segment plots (the the hmmcopy segments)
        - bias plots ( for the wig file correction)
        - correction plots (for wig file correction) 
    """

    def __init__(self, component_name="plot_hmmcopy", 
                 component_parent_dir=None, seed_dir=None):
        
        ## TODO: pass the version of the component here.
        self.version = "1.0.1"

        ## initialize ComponentAbstract
        super(Component, self).__init__(component_name, 
                                        component_parent_dir, seed_dir)

    def make_cmd(self, chunk=None):
        path = os.path.join(self.seed_dir, 'plot_hmmcopy.R')

        cmd = ' '.join([self.requirements['R']+'script', path])

        cmd_args = [self.args.tumour_copy, self.args.hmmcopy_res,
                    self.args.correction_plots_dir,
                    self.args.bias_plots,
                    self.args.hmmcopy_plots_dir]
        return cmd, cmd_args

## To run as stand alone
def _main():
    m = Component()
    m.args = component_ui.args
    m.run()

if __name__ == '__main__':
    import component_ui
    _main()

