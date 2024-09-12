from qgis.PyQt.QtWidgets import QDialog

from arho_feature_template.core.feature_template import FeatureTemplate


class AddFeatureForm(QDialog):
    """Dialog for filling and saving attribute data that opens when a new feature has been digitized."""

    def __init__(self, feature_template: FeatureTemplate):
        self.feature_template = feature_template

    def _init_feature_attributes(self):
        # for feature_attribute in self.feature_template.feature_attributes:
            # # Create the form here, add rows with labels and input fields
        pass

    def save(self):
        pass
