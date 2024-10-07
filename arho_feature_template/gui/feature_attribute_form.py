from __future__ import annotations

from collections import defaultdict
from importlib import resources
from typing import TYPE_CHECKING

from qgis.PyQt import uic
from qgis.PyQt.QtWidgets import QDialog, QLineEdit

if TYPE_CHECKING:
    from qgis.PyQt.QtWidgets import QDialogButtonBox, QFormLayout, QWidget

    from arho_feature_template.core.template_library_config import Feature

ui_path = resources.files(__package__) / "feature_attribute_form.ui"
FormClass, _ = uic.loadUiType(ui_path)


class FeatureAttributeForm(QDialog, FormClass):  # type: ignore
    """Parent class for feature forms for adding and modifying feature attribute data."""

    attribute_form_layout: QFormLayout
    button_box: QDialogButtonBox

    def __init__(self, feature_template_config: Feature):
        super().__init__()
        self.setupUi(self)

        self.attribute_widgets: dict[str, dict[str, QWidget]] = defaultdict(dict)

        layer = feature_template_config.layer
        for attribute_config in feature_template_config.attributes:
            field = QLineEdit()
            self.attribute_form_layout.addRow(attribute_config.attribute, field)
            self.attribute_widgets[layer][attribute_config.attribute] = field
