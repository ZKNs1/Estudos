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
- `git aplly`
- `git commit-tree`
- `git hash-object`
