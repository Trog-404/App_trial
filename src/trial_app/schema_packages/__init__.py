from nomad.config.models.plugins import SchemaPackageEntryPoint
from pydantic import Field


class NewSchemaPackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from trial_app.schema_packages.schema_package import m_package

        return m_package


schema_package_entry_point = NewSchemaPackageEntryPoint(
    name='NewSchemaPackage',
    description='New schema package entry point configuration.',
)

class ProvaEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from trial_app.schema_packages.fabrication_process import m_package

        return m_package


prova_entry_point = ProvaEntryPoint(
    name='Prova',
    description='Schema package for describing a fabrication process.',
)
