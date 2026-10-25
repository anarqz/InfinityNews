O seu progresso é a coisa mais importante que você traz para o Infinity, então aqui vai exatamente como o launcher cuida dos seus saves.

## Os saves ficam onde o jogo coloca

O Infinity não guarda cópia dos seus saves em nenhum outro lugar. Eles ficam na própria pasta de saves do Azimuth:

`<Azimuth>\data\titles\1A96545B\saves\player-1\`

## Os mesmos perfis offline e online

Você tem até três perfis, com ou sem login, e todos jogam tanto offline quanto online. Cada perfil tem a sua própria identidade e, portanto, a sua própria pasta de save (`User_…`), lado a lado em `player-1`. Perfis nunca compartilham um save.

- **Um perfil criado sem entrar** (só Noob) registra o nome na próxima vez que você entrar. Se alguém pegou esse nome nesse meio-tempo, o launcher pede outro; o perfil e o save dele ficam exatamente como estão.
- **Perfis Noob** usam uma única pasta de save offline e online: o que você faz offline continua online, e vice-versa.
- **O Hardcore** funciona diferente: online, ele sempre continua a sua carreira da nuvem. Jogado offline, um perfil Hardcore guarda esse progresso numa pasta local separada que nunca é enviada.

## Revisões: o jogo guarda as duas mais novas

Cada vez que o jogo salva, ele grava uma nova *revisão*. Uma revisão só vale quando está completa: todos os arquivos batem com a lista que o jogo gravou junto. O jogo sempre carrega a revisão completa mais nova e guarda as duas mais recentes.

## Comece por um save que você já tem

Ao criar um perfil, você pode começar a partir de qualquer save que já esteja no seu PC — eles aparecem do mais recente para o mais antigo, com nível e créditos. O seu save original é só lido, nunca alterado. O launcher faz uma cópia, confere cada arquivo e só então transforma essa cópia na revisão mais nova do perfil. Isso só acontece com o jogo fechado, e se algo der errado no meio do caminho, o perfil fica exatamente como estava.

## Nada é apagado

Sempre que o launcher precisa tirar algo do caminho — uma revisão incompleta, um save mais antigo que ele substitui, uma versão da nuvem, um conflito — ele primeiro copia para:

`saves\fi-launcher-archive\<User_…>\`

## Saves na nuvem

Só os perfis **Infinity Supporter** no modo **Hardcore** têm save na nuvem. Todos os outros perfis ficam apenas no seu PC.

Para esses perfis, a cada sessão de jogo:

- **Antes de o jogo abrir,** o launcher reenvia o que não subiu da última vez, separa revisões incompletas e instala uma revisão mais nova da nuvem, se houver.
- **Se algo parecer errado,** como um conflito ou um save ainda sendo gravado, o jogo não abre em vez de arriscar.
- **Depois que você sai,** a sua revisão completa mais nova é enviada. Se o envio falhar, ele fica pendente e é tentado de novo na próxima vez que você abrir o jogo.

## Pinturas são por PC

As suas criações (pinturas e as miniaturas delas) são compartilhadas por todos os perfis do mesmo PC e não vão para a nuvem.

## Bons hábitos

- Feche o jogo antes de mexer na pasta de saves.
- De vez em quando, faça o seu próprio backup de `player-1` — não custa nada.
