
from qgis.PyQt.QtWidgets import QWidget

from arho_feature_template.core.feature_template_library import FeatureTemplateLibrary
from arho_feature_template.qgis_plugin_tools.tools.resources import load_ui  # noqa F401


# class AddFeaturePanel(QWidget, load_ui("add_feature_panel.ui")):  # NOTE: UI file does not exist yet
class AddFeaturePanel(QWidget):
    """Dock widget for selecting a feature template."""

    def __init__(self, feature_template_library: FeatureTemplateLibrary):
        super().__init__()
        # self.setupUi(self)
        self.initialize_from_library(feature_template_library)


    def initialize_from_library(self, feature_template_library: FeatureTemplateLibrary):
        # Initialization logic
        self.library = feature_template_library
