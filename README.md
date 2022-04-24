[![Docker](https://badgen.net/badge/icon/docker?icon=docker&label)](https://https://docker.com/)
[![CI](https://github.com/agn-7/bitpin-project/workflows/build/badge.svg)](https://github.com/agn-7/bitpin-project/actions/workflows/github-actions.yml)
[![codecov](https://codecov.io/gh/agn-7/bitpin-project/branch/main/graph/badge.svg?style=flat-square)](https://codecov.io/gh/agn-7/bitpin-project) 
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black) 

# bitpin-project

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`api/v1/content/` | GET | READ | Get all contents
`api/v1/rate/:content_id` | POST | CREATE | Create a new vote
`api/v1/rate`| POST | CREATE | Create a new vote
`api-token-auth/` | POST | READ | Get token
