import pyenzyme as pe

from pyenzyme.thinlayers import ThinLayerCopasi, ThinLayerPysces
from zntrack import Node, zn

from .model import Model

class ParameterEstimation(Node):
    
    # Dependencies
    data: Model = zn.deps()
    
    # Parameters
    thinlayer: str = zn.params()
    
    # Metrics
    parameters: dict = zn.metrics()
    
    # Plots
    time_course = zn.plots(x_label="Time", y_label="Concentration")
    
    def run(self):
        """Performs parameter estimation using COPASI"""
        
        # Write OMEX to read
        self.data.enzmldoc.toFile(".", "document")
        
        if self.thinlayer.lower() == "copasi":
            # Initialize COPASI Thin Layer
            thinlayer = ThinLayerCopasi(
                "document.omex", "COPASI"
            )
        elif self.thinlayer.lower() == "pysces":
            # Initialize PySCeS Thin Layer
            thinlayer = ThinLayerPysces(
                "document.omex", "PySCeS"
            )
        else:
            raise KeyError(
                f"Thin layer {self.thinlayer} does not exist. Please use either `copasi` or `pysces`"
            )
        
        # Perform estimation
        thinlayer.optimize()
        modelled = thinlayer.write()
        
        # Extract parameters to metrics
        self.parameters = {
            f"{reaction.id}_{parameter.name}": parameter.value
            for reaction in modelled.reaction_dict.values()
            for parameter in reaction.model.parameters
        }