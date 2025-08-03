resource "azurerm_role_assignment" "app_role" {
  scope                = azurerm_resource_group.main.id
  role_definition_name = "Reader"
  principal_id         = "<service_principal_object_id>"
}
