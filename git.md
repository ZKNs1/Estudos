# Git
Sistema de controle de versão distribuído (VCS), uma ferramenta por linha de comando. 

É muito utilizado para:
- Manter histórico de alterações no código;
- Reverter erros no código;
- Colaboração entre desenvolvedores;
- Backups do código

## Sintaxe de Comando

```bash
command <required> [optional]
```
- Argumentos entre `< >` são obrigatórios e deve ser fornecido ao executar o comando;
-  Argumentos entre `[ ]` são opcionais e podem ser incluídos caso necessário.

Exemplo:
```bash
mkdir <directory-name>
```
- `mkdir` é o comando
- `<directory-name>` é o argumento obrigatório.

## Manual
Para mostrar o manual:
```bash
man git
```

**Atalhos:**
- `q` sai do manual;
- `j` desce uma linha;
- `k` sobe uma linha;
- `d` desce meia página;
- `u` sobe meia página;
- `/<term>` procura por um termo;
- `n` próximo termo;
- `N` termo anterior.

## Porcelain e Plumbing
No Git os comandos são dividos em comandos de alto nível (porcelain) e baixo nível (plumbing).

**Porcelain**
São os mais utilizados para interagir com o código.
Exemplo: 
- `git status`
- `git add`
- `git commit`
- `git push`
- `git pull`
- `git log`

**Plumbing**
Exemplos: 
- `git apply`
- `git commit-tree`
- `git hash-object`

## Configuração

Toda vez que o código é alterado o git rastreia quem fez a alteração, por isso é preciso definir seu nome e e-mail. No Git temos configurações nível global e nivél do repositório, na maioria das vezes utilizamos as globais.

O primeiro passo para qualquer projeto é a criação 
de um repositório, que é um diretório que contém seu projeto e a pasta `.git` que armazena informações de versionamento do projeto e a rastreabilidade interna.

## Status
- `untracked`: não está sendo rastreado pelo Git;
- `staged`: marcado para incluir no próximo commit;
- `committed`: salvo no histórico do repositório.

## Git Log
Mostra todo o histórico de commits do repositório, oferecendo informações como quem fez o commit, quando o commit foi feito e o que foi alterado.

**Hash**

Todo commit tem um identificador único que é uma longa string de caracteres. Esse hash é gerado a partir da mensagem do commit, do nome e e-mail do autor, o dia e a hora do commit e hashes de commits anteriores.

Exemplo:
```bash
5ba786fcc93e8092831c01e71444b9baa2228a4f
```

Para facilitar você pode se referir a um commit utilizando os 7 primeiros caracteres de seu hash, seguindo o exemplo: `5ba786f`.

## Plumbing

Todos os dados de um repositório são armazenados no diretório oculto `.git`, dados como os commits, branches, tags e outros objetos. O Git é composto por diversos objetos que são armazenados no `.git/objects`, um commit é um tipo de objeto.
