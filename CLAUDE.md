# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a configuration repository containing MS SQL Server database connection settings. The main file `Lista baz danych.xml` (Polish for "Database List") stores serialized .NET XML configuration for 65+ database connections.

## Repository Structure

- `Lista baz danych.xml` - Main configuration file containing `DatabaseCollection` with `MsSqlDatabase` entries

## Database Entry Schema

Each `<MsSqlDatabase>` element contains:
- **Identity**: `Name`, `Description`, `Active`, `OperatorName`
- **Connection**: `Server`, `DatabaseName`, `Timeout`, `UseConnectionString`
- **Authentication**: `WindowsAuthentication`, `Trusted`, `User`, `Password` (encrypted with `=` prefix)
- **Performance**: `BatchLinks`, `BatchFeatures`, `BatchSubTables`, `NonCollectedRows`
- **Flags**: `UpdateFeaturesLegacyMode`, `ChangeInfoLegacyMode`, `IsOptimalization`, `LockNotification`, `TrustServerCertificate`, `MultiSubnetFailover`
- **Licensing**: `VirtualTeleKeySerial`, `LicencesSelection`

## Working with This Repository

**XML Validation**: Ensure valid XML structure when editing. The file uses UTF-8 encoding with BOM.

**Password Fields**: Passwords are encrypted using a custom scheme (hex string prefixed with `=`). Do not modify encrypted values directly.

**Adding New Database Entry**: Copy an existing `<MsSqlDatabase>` block and modify the required fields. Typical defaults:
- `BatchLinks=100`, `BatchFeatures=100`, `BatchSubTables=40`
- `NonCollectedRows=50000`, `Timeout=15`
- `IsOptimalization=true`, `TrustServerCertificate=true`
