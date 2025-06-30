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
- `git config`: interagir com as configurações do Git;
- `--add`: adicionar uma configuração;
- `--global`: salvar a configuração globalmente;
- `--local`: salvar a configuração no repositório local;
- `--list`: lista das configurações;
- `--get`: conseguir valores (`git config --get <key>`);
- `<key>`: `<section>.<keyname>`, exemplo: user.name, webflyx.ceo;
- `--unset`: utilizado para remover um valor de uma configuração;
- `--unset-all`: remove tudo de uma key na sua configuração;
- `--remove-section`: remove uma seção inteira da configuração (`git config --remove-section section`);

## Locais de Configuração
- system: `/etc/gitconfig` configura o Git para todos os usuários do sistema;
- global: `~/.gitconfig` configura o Git para todos os projetos de um usuário;
- local: `.git/config` configura o Git para um projeto específico;
- worktree: `.git/config/worktree` configura o Git para parte de um projeto.

**Overrinding**
Se você definir uma configuração num local específico, ela vai substituir a configuração que foi definida de forma geral. Exemplo se eu definir `user.name` na configuração local, ela vai sobrepor o `user.name` definido na configuração global.

![image](https://github.com/user-attachments/assets/77574cef-afdf-439e-a057-d953e809864f)

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

## Cat File

O Git criou o comando `cat-file` para permitir a gente ver os conteúdos do commit sem ter que ficar navegando pelos arquivos de objeto.

```bash
git cat-file -p <hash>
```

```bash
catfile-command-here > /tmp/catfileout.txt
git cat-file -p d5d5c951595fe4a03627e9770dc925838cc7650b > /tmp/catfileout.txt
```

## Trees and Blobs
- Tree: jeito do Git de armazenar um diretório;
- Blob: jeito do Git de armazenar um arquivo.

```bash
git cat-file -p <hash>
git cat-file -p <tree>
git cat-file -p <blob>
```

## Armazenamento de dados
O Git armazena uma snapshot (imagens) dos arquivos de cada commit, por conta disso ele também possui otimizações de desempenho, para que o repositório `.git` não fique grande e pesado demais.

Essa otimização de desempenho ocorre com o Git comprimindo e agrupando os arquivos, para armazenar de forma mais eficiente, ele também só armazena um novo arquivo caso haja uma mudança num arquivo do commit.
