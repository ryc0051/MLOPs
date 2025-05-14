terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~>4.2"
    }
  }
}

provider "azurerm" {
  subscription_id =  "436ae9d6-a5d3-4a84-851a-19bf6e053931"
  features {}
  
}

resource "azurerm_resource_group" "kubernetesragroup" {
    name     = "kubernetes-rg"
    location = "australiaeast"
}

resource "azurerm_storage_account" "terraformstorage" {
    name                     = "rycterraformstorage"
    resource_group_name      = azurerm_resource_group.kubernetesragroup.name
    location                 = azurerm_resource_group.kubernetesragroup.location
    account_tier             = "Standard"
    account_replication_type = "LRS"
}