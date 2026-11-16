Infinity Horizon 1.0.3

### Download
Download **infinity-horizon-1.0.3-windows-x64.zip**, extract the entire archive into its own folder outside the Azimuth installation, and run **infinity.exe**. Keep all bundled files and signature sidecars together. Use **Configure** to install the included hook 79 before playing online.

### Changes
- Improve UDP discovery by comparing fresh IPv4 observations from independent STUN providers.
- Retry STUN discovery when the first request is lost.
- Preserve valid connection candidates during ordinary session updates.
- Improve lobby-switch and existing-seat handling.
- Add bounded connection diagnostics and retain logs from previous runs.

The package includes the Windows x64 launcher, updater, hook, overlay, English/Portuguese translations and license notices. Game and Azimuth files are not included. Windows and isolated Proton checks passed; connectivity between different home networks still needs gameplay validation.

The JSON descriptor and detached signature support authenticated automatic updates.

**SHA-256 (ZIP):** `c03687f433a03de429a48b2368290fb9f70e01ae96e549df209d481f94a69ae9`

### Português
Baixe o ZIP, extraia todo o conteúdo em uma pasta própria fora da instalação do Azimuth e execute **infinity.exe**. Use **Configure** para instalar o hook 79 antes de jogar online.

Esta versão corrige problemas na descoberta UDP, preserva candidatos válidos de conexão, melhora a troca de lobbies e adiciona logs de diagnóstico limitados. Os testes no Windows e no Proton passaram; a conexão entre redes domésticas distintas ainda precisa de validação em partida. Arquivos do jogo e do Azimuth não estão incluídos.

[Download and full notes](https://github.com/anarqz/InfinityHorizon/releases/tag/v1.0.3)
