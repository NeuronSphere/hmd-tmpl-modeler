# Changelog

## 2026-10-23

- fix: generated microservices build on `ghcr.io/hmdlabs/hmd-ms-base:0.2.285` (was `neuronsphere/hmd-ms-base:stable`), the first base image verified to reject the compromised eMudhra chains (`certifi==2026.10.19`), with `PYTHONPATH` on its python3.11 site-packages. Earlier images carried a certifi that still trusts the eight eMudhra intermediate CAs whose private keys were disclosed on 2026-10-20.

## 2025-06-30

- feat: adds _utils template to templates.json

## 2024-12-03

- fix: renames packages to modules
- feat: adds templates json file

## 2024-12-02

- feat: adds django artifact templates

## 2024-04-03

- fix: fixes M -> 1 templates

## 2024-04-01

- feat: setups up mickey config

## 2024-03-13

- fix: fixes attributes macros
- fix: reverts last change

## 2024-03-12

- fix: fixes typescript lib templates

## 2024-03-06

- fix: fixes pretty printing json
- feat: adds raw model dump template

## 2024-03-05

- fix: fixes microservice setup.py
- fix: fixes config_local.json
- fix: fixes config_local.json
- fix: adds config_local.json to microservice
- fix: adds VERSION file to microservice
- feat: adds postgres ddl and microservice templates

## 2024-03-01

- fix: fixes docs index.rst template
- fix: fixes rst templates
- fix: fixes utils import
- feat: adds initial templates
- feat: :tada: generate initial repo structure
