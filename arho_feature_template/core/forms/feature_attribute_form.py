from qgis.PyQt.QtWidgets import QDialog

from arho_feature_template.core.feature_template import FeatureTemplate
from arho_feature_template.qgis_plugin_tools.tools.resources import load_ui


class FeatureAttributeForm(QDialog, load_ui("feature_attribute_form.ui")):
    """Parent class for feature forms for adding and modifying feature attribute data."""

    def __init__(self, feature_template: FeatureTemplate):
        super().__init__()
        self.setupUi(self)
        self.feature_template = feature_template
