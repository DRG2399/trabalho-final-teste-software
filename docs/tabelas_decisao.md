# Tabelas de Decisao
Este documento apresenta tabelas de decisao para os dois principais fluxos da aplicacao: login e formulario de contato.

## Login
|--------------------------------------------------------------------------------------------------------------------------|
| Regra | Usuario preenchido | Senha preenchida | Usuario existe | Senha correta | Resultado esperado                      |
|--------------------------------------------------------------------------------------------------------------------------|
| L1    | Nao                | Nao              | Nao avaliado   | Nao avaliado  | Exibir erro: preencher usuario e senha  |
| L2    | Sim                | Nao              | Nao avaliado   | Nao avaliado  | Exibir erro: preencher usuario e senha  |
| L3    | Nao                | Sim              | Nao avaliado   | Nao avaliado  | Exibir erro: preencher usuario e senha  |
| L4    | Sim                | Sim              | Nao            | Nao avaliado  | Exibir erro: usuario ou senha invalidos |
| L5    | Sim                | Sim              | Sim            | Nao           | Exibir erro: usuario ou senha invalidos |
| L6    | Sim                | Sim              | Sim            | Sim           | Redirecionar para o dashboard           |
|--------------------------------------------------------------------------------------------------------------------------|

## Formulario de Contato
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Regra | Nome preenchido | Email preenchido | Email valido | Mensagem preenchida | Mensagem com tamanho minimo | Resultado esperado                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| C1    | Nao             | Nao avaliado     | Nao avaliado | Nao avaliado        | Nao avaliado                | Exibir erro: nome obrigatorio                    |
| C2    | Sim             | Nao              | Nao avaliado | Nao avaliado        | Nao avaliado                | Exibir erro: email obrigatorio                   |
| C3    | Sim             | Sim              | Nao          | Nao avaliado        | Nao avaliado                | Exibir erro: email invalido                      |
| C4    | Sim             | Sim              | Sim          | Nao                 | Nao avaliado                | Exibir erro: mensagem obrigatoria                |
| C5    | Sim             | Sim              | Sim          | Sim                 | Nao                         | Exibir erro: mensagem com menos de 10 caracteres |
| C6    | Sim             | Sim              | Sim          | Sim                 | Sim                         | Exibir mensagem de sucesso                       |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|