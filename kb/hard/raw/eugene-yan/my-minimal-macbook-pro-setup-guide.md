# My Minimal MacBook Pro Setup Guide

**Source:** https://eugeneyan.com//writing/mac-setup/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** recsys, ml-systems

---

I just upgraded my personal laptop from a 2019 Intel MacBook Pro to an M4 MacBook Pro. Like all my new devices, instead of restoring from a backup, I try to Marie Kondo my digital life and start from a clean slate. This also lets me reexamine my existing tools and explore new options. Here’s my minimal Mac setup guide if you want to follow along.

* [MacOS settings](#macos-settings)
* [Basic developer tools](#basic-developer-tools)
* [Research, writing, development](#research-writing-development)
* [Productivity and quality of life](#productivity-and-quality-of-life)
* [Entertainment and communications](#entertainment-and-communications)

## MacOS settings

* **Apple ID**: Sign in
* **MacOS update**: Settings -> General -> Software Update
* **Keyboard**: Switch to Dvorak, key repeat = fast, delay until repeat = short
* **Trackpad**: Max tracking speed, tap to click, click = light, natural scroll = off
* **Displays**: Switch to Apple Display (p3-600) for slightly better battery life
* **Finder**: Show Library, show hidden files, show path to dir

```
# show Library folder
chflags nohidden ~/Library

# show hidden files
defaults write com.apple.finder AppleShowAllFiles YES

# add pathbar to title
defaults write com.apple.finder _FXShowPosixPathInTitle -bool true

# restart finder
killall Finder;
```

* **Screenshots** (to clipboard): `CMD + SHIFT + F5` and change setting in “Option” menu. This lets me screenshot and paste into docs, chats, social media, etc directly (without saving a separate file). If I need to save it, open Preview and `CMD + N`.
* **Dock**: Hide and show dock, reduce size, remove most default apps

## Basic developer tools

* **Homebrew** (might take a while as it also installs Xcode)

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# add brew to default shell path
echo >> /Users/eugeneyan/.zprofile
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/eugeneyan/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"

# check for updates
brew update
```

* **Terminal**: Trying Warp instead of my usual iTerm. (If you use [my referral code](https://app.warp.dev/referral/D9WZNJ) I can get some swag—thank you!)

```
brew install --cask warp
brew install --cask font-inconsolata-for-powerline
# Update warp font: Settings -> Appearance -> Terminal font
```

* **Shell**: Trying Fish instead of my usual Oh My Zsh

```
brew install fish

# make fish default shell
echo $(which fish) | sudo tee -a /etc/shells
chsh -s $(which fish)

# add brew to fish path
echo >> /Users/eugeneyan/.config/fish/config.fish
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/eugeneyan/.config/fish/config.fish
eval "$(/opt/homebrew/bin/brew shellenv)"
```

* **Htop**: A better top

```
brew install htop
```

* **New SSH keys**

```
ssh-keygen -t ed25519 -C "[email protected]"

eval "$(ssh-agent -s)"
touch ~/.ssh/config
open ~/.ssh/config

# add to config
Host github.com
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
```

Also see the Github docs to [generate a new ssh key and add to ssh agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent), and [add a new ssh key to Github account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).

* **Git**

```
brew install git
git config --global init.defaultBranch main
git config --global user.name "eugeneyan"
git config --global user.email [email protected]
```

## Research, writing, development

* **Obsidian**: All my notes, writing, CRM, etc. live here

```
brew install --cask obsidian

# clone obsidian vault (i use obsidian-git for syncing)
git clone [email protected]:<github-username>/<obsidian-vault>.git
```

* **Zotero**: Papers and annotations. Zotero has a nice PDF reader and markup tools, and also has an iPad app that syncs seamlessly. (Previously Google Drive)

```
brew install --cask zotero
# enable zotero plugin in safari
```

* **Cursor**: Daily driver for prototyping and building. (Previously vscode)

```
brew install --cask cursor
# old machine: cmd+shift+p > export profile
# new machine: cmd+shift+p > import profile
```

* **Sublime**: Simple code and text edits

```
brew install --cask sublime-text
```

* **Chrome**: For web development

```
brew install --cask google-chrome
```

* **Postgres**: To prototype web apps that need persistent storage

```
brew install postgresql@16
```

* **Python, JS, and Ruby**

```
# very fast python package manager
brew install uv

# install the latest python
uv python install 3.12
```

```
brew install node
brew install nvm

# still deciding between pnpm and bun
brew install pnpm
brew install oven-sh/bun/bun
```

```
brew install chruby-fish ruby-install ruby-build
brew install rbenv

# workaround for fish shell
set --universal fish_user_paths $fish_user_paths ~/.rbenv/shims
rbenv global 3.3.5
rbenv rehash
```

* **Docker**

```
brew install --cask docker
```

* **Ollama + Open WebUI**: Running local models via a nice interface

```
brew install ollama
ollama serve

# in another terminal, pull some models to try
ollama pull llama3.2 nemotron  # 3B and 70B respectively
```

```
uv tool install open-webui
uv tool run open-webui serve
```

## Productivity and quality of life

* **Raycast**: A better spotlight

```
brew install --cask raycast
```

* **Rectangle**: Window management.

```
brew install --cask rectangle
```

While Raycast already has window management, Rectangle lets you hit the hotkey again (e.g., `CTRL + CMD + LEFT`) to resize windows from 1/3 to 1/2 to 2/3. Great for widescreens.

Rectangle settings for resizing windows

> Update: Turns out Raycast has this too ([h/t @mwheatfill](https://x.com/mwheatfill/status/1859094246101279085)), and also has presets for Rectangle hotkeys. I’ve since moved to Raycast window management.

* **Wispr Flow**: [Download](https://www.flowvoice.ai/download) and set output language = English. Speech-to-text. Returns accurate transcripts with decent punctuation and formatting. (If you use [my referral link](https://www.flowvoice.ai/?referral=EUGENE11) you earn good karma and I get $15 in credits! )
* **Google Drive**: Syncing documents, files, media, etc.

```
brew install --cask google-drive
```

* **Stats + Ice**: Adding system stats to menu bar and customizing the menu bar

```
brew install stats
brew install jordanbaird-ice
```

* **Logi Options+** [Download](https://www.logitech.com/en-us/software/logi-options-plus.html) and sign in to load saved settings for my [MX Ergo](https://www.logitech.com/en-us/products/mice/mx-ergo-wireless-trackball-mouse.html).

## Entertainment and communications

* **Media**

```
brew install --cask vlc
brew install --cask spotify
```

* **Chat**

```
brew install --cask telegram
brew install --cask discord
brew install --cask slack
```

## References

* [Tweet thread with lots of great suggestions](https://x.com/eugeneyan/status/1857234166800367812)
* [Swyx’s Mac setup](https://www.swyx.io/new-mac-setup)
* [Sourabh Bajaj’s Mac Setup](https://sourabhbajaj.com/mac-setup/)
* [Robin Wieruch’s Mac Setup](https://www.robinwieruch.de/mac-setup-web-development/)
* [Tania Rascia’s Mac Setup](https://www.taniarascia.com/setting-up-a-brand-new-mac-for-development/)
* [Thorsten Ball’s Mac Setup](https://registerspill.thorstenball.com/p/new-year-new-job-new-machine)
* [Mimansa Jaiswal’s Mac Setup](https://mimansajaiswal.github.io/posts/mac-softwares/)

  

If you found this useful, please cite this write-up as:

> Yan, Ziyou. (Nov 2024). My Minimal MacBook Pro Setup Guide. eugeneyan.com.
> https://eugeneyan.com/writing/mac-setup/.

or

```
@article{yan2024macsetup,
  title   = {My Minimal MacBook Pro Setup Guide},
  author  = {Yan, Ziyou},
  journal = {eugeneyan.com},
  year    = {2024},
  month   = {Nov},
  url     = {https://eugeneyan.com/writing/mac-setup/}
}
```

  
Share on:
