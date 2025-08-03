resource "azurerm_cognitive_account" "openai" {
  name                  = "rag-openai"
  location              = var.location
  resource_group_name   = azurerm_resource_group.main.name
  kind                  = "OpenAI"
  sku_name              = "S0" # Free Tier
  custom_subdomain_name = "ragopenai"
}

resource "azurerm_cognitive_deployment" "embedding_model" {
  name                 = "embedding"
  cognitive_account_id = azurerm_cognitive_account.openai.id
  model {
    format  = "OpenAI"
    name    = "text-embedding-ada-002"
    version = "1"
  }
  scale {
    type = "Standard"
  }
}

resource "azurerm_cognitive_deployment" "chat_model" {
  name                 = "chat"
  cognitive_account_id = azurerm_cognitive_account.openai.id
  model {
    format  = "OpenAI"
    name    = "gpt-35-turbo"
    version = "0301"
  }
  scale {
    type = "Standard"
  }
}
