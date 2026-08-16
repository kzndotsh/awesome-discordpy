<!-- title -->

<!--lint ignore no-dead-urls-->
<!--lint disable awesome-heading-->
# Awesome Discord.py List

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![lint](https://github.com/kzndotsh/awesome-discordpy/actions/workflows/lint.yaml/badge.svg)](https://github.com/kzndotsh/awesome-discordpy/actions/workflows/lint.yaml)

<!-- subtitle -->

An Awesome list for all things Discord.py

<!-- image -->

![Discord.py Logo](assets/banner.png)

<!-- description -->

[Discord.py](https://discordpy.readthedocs.io/en/stable/) is a modern, easy to use, feature-rich, and async ready API wrapper for Discord.

<!-- TOC -->

## Contents

<!--lint disable awesome-toc-->
- [Awesome Discord.py List](#awesome-discordpy-list)
  - [Contents](#contents)
  - [Official Links](#official-links)
  - [Libraries and Extensions](#libraries-and-extensions)
    - [Utilities](#utilities)
    - [Testing and Debugging](#testing-and-debugging)
    - [UI - Pagination, Menus, Embeds and similar](#ui---pagination-menus-embeds-and-similar)
    - [Inter-Process Communication](#inter-process-communication)
    - [Voice and Audio](#voice-and-audio)
    - [Authentication](#authentication)
    - [Metrics, Monitoring, and Logging](#metrics-monitoring-and-logging)
    - [Miscellaneous](#miscellaneous)
    - [Templates](#templates)
  - [Example Bots](#example-bots)
  - [Blog Posts, Guides and Tutorials](#blog-posts-guides-and-tutorials)
  - [Community Gists and Snippets](#community-gists-and-snippets)
  - [Additional Resources](#additional-resources)
  - [Forks and Wrappers](#forks-and-wrappers)
  - [Archived/Deprecated](#archiveddeprecated)
  - [Contributing](#contributing)
    - [Contributors](#contributors)

<!-- CONTENT -->

## Official Links

- [Discord.py Documentation](https://discordpy.readthedocs.io/en/latest/) - Official documentation for Discord.py.
- [Discord.py Changelog](https://discordpy.readthedocs.io/en/latest/whats_new.html) - Official changelog for Discord.py.
- [Discord.py FAQ](https://discordpy.readthedocs.io/en/latest/faq.html) - Official frequently asked questions for discord.py.
- [Migrating to v2.0](https://discordpy.readthedocs.io/en/latest/migrating.html) - Official breaking-change guide for discord.py 2.0.
- [Discord.py Quickstart](https://discordpy.readthedocs.io/en/latest/quickstart.html) - Official getting-started guide.
- [Official Examples](https://github.com/Rapptz/discord.py/tree/master/examples) - Example bots and snippets from the discord.py repository.
- [Discord.py GitHub](https://github.com/Rapptz/discord.py) - Official GitHub repository for Discord.py.
- [Discord.py Discord Server](https://discord.gg/dpy) - Official Discord server for Discord.py.

## Libraries and Extensions

### Utilities

- [InterStella0/starlight-dpy](https://github.com/InterStella0/starlight-dpy) - A utility library for discord.py.
- [clari7744/DPyUtils](https://github.com/clari7744/DPyUtils) - Some extra discord.py additions such as duration utilities, converters, a context editor and more.
- [tanrbobanr/dpy-check](https://github.com/tanrbobanr/dpy-check) - A system for making more dynamic and complex checks on discord.py commands.
- [robertwayne/cogwatch](https://github.com/robertwayne/cogwatch) - Hot-reloading for discord.py-based command files.
- [timelessnesses/dpyhr](https://github.com/timelessnesses/dpyhr) - Dpyhr is a hot cog reloader (that uses discord.py cog's implementation) to reload anytime you wanted to save.
- [mikeshardmind/discord-scheduler](https://github.com/mikeshardmind/discord-scheduler) - A persistent scheduling implementation suitable for use with discord.py.
- [Voxel-Fox-Ltd/VoxelBotUtils](https://github.com/Voxel-Fox-Ltd/VoxelBotUtils) - An extension of discord.py that adds helpers for bot setup, commands, and common patterns.
- [Kyrela/discore](https://github.com/Kyrela/discore) - A small core for initializing discord.py bots and tracking logs and errors.
- [LiBa001/disputils](https://github.com/LiBa001/disputils) - Pagination, confirmation, and other small discord.py UI utilities.
- [Soheab/discord.py-listen-overloads](https://github.com/Soheab/discord.py-listen-overloads) - Type stubs that add overloads to `@commands.Bot.listen` for discord.py events.
- [Soheab/discord-ext-subcommands](https://github.com/Soheab/discord-ext-subcommands) - Define prefix, slash, and hybrid subcommands across multiple files and cogs.
- [Soheab/discord-ext-custom_interaction](https://github.com/Soheab/discord-ext-custom_interaction) - Subclass `discord.Interaction` to add helpers such as `send` and `author`.

### Testing and Debugging

- [scarletcafe/jishaku](https://github.com/scarletcafe/jishaku) - A debugging and testing cog for discord.py rewrite bots.
- [CraftSpider/dpytest](https://github.com/CraftSpider/dpytest) - A package that assists in writing tests for discord.py.
- [wasi-master/dpylint](https://github.com/wasi-master/dpylint) - A Pylint plugin for linting discord.py bot code.

### UI - Pagination, Menus, Embeds and similar

- [Defxult/reactionmenu](https://github.com/Defxult/reactionmenu) - A library to create a discord.py 2.0+ paginator. Supports pagination with buttons, reactions, and category selection using selects.
- [Soheab/discord-py-paginators](https://github.com/Soheab/discord-py-paginators) - An extension for discord.py that provides various paginators.
- [Soheab/modal-paginator](https://github.com/Soheab/modal-paginator) - An extension for discord.py that allows you to paginate a Modal using buttons.
- [philskillz-coder/discord-py-paginator](https://github.com/philskillz-coder/discord-py-paginator) - A view paginator for discord.py.
- [Ikusaba-san/dpy-ui](https://github.com/Ikusaba-san/dpy-ui) - An extension of discord.py that makes prompting users and pagination easier.
- [thegamecracks/discord-ext-pager](https://github.com/thegamecracks/discord-ext-pager) - A discord.py 2.0 paginator library with a similar interface to discord-ext-menus.
- [OnceYT/dpy-paginator](https://github.com/OnceYT/dpy-paginator) - A discord.py utility with no external dependencies that makes paginating embeds easier.
- [Soheab/discord-ext-embeds](https://github.com/Soheab/discord-ext-embeds) - An extension for discord.py that adds a few nice-to-have features to discord.py's embed.
- [keizaiya/discord-ext-flow](https://github.com/keizaiya/discord-ext-flow) - This library extends discord.ui, providing UI control based on state flows.
- [sizumita/discord-ext-ui](https://github.com/sizumita/discord-ext-ui) - An extension of discord-ui that adds some quality-of-life features.
- [Seniatical/dpy-paginator](https://github.com/Seniatical/dpy-paginator) -  A simple pagination library for discord.py, comes with support for dropdown, button based pagination.
- [vcv88/discord-ext-dyn](https://github.com/vcv88/discord-ext-dyn) - An extension for handling dynamic modals/buttons/select menus.
- [oliver-ni/discord-ext-menus-views](https://github.com/oliver-ni/discord-ext-menus-views) - A thin layer over discord.ext.menus that uses discord.py v2 views instead of reactions.
- [Modern-Realm/discord_btns_menus](https://github.com/Modern-Realm/discord_btns_menus) - Helpers for buttons, select menus, combinations, and pagination on discord.py and related forks.
- [Rapptz/discord-ext-menus](https://github.com/Rapptz/discord-ext-menus) - Experimental reaction-menu and pagination helpers from the discord.py author.
- [HollowTheSilver/CascadeUI](https://github.com/HollowTheSilver/CascadeUI) - A Redux-inspired UI framework for discord.py with Components V2, persistence, and pre-built patterns.

### Inter-Process Communication

- [MiroslavRosenov/better-ipc](https://github.com/MiroslavRosenov/better-ipc) - High-performance inter-process communication library designed to work with the latest version of discord.py.
- [No767/discord-ext-ipcx](https://github.com/No767/discord-ext-ipcx) - An maintained discord.py extension for inter-process communication.

### Voice and Audio

- [discord-ext-voice-recv](https://github.com/imayhaveborkedit/discord-ext-voice-recv) - Voice receive extension package for discord.py.
- [Sheppsu/discord-ext-listening](https://github.com/Sheppsu/discord-ext-listening) - Voice receive extension for discord.py built on multiprocessing and designed to be flexible.
- [PythonistaGuild/Wavelink](https://github.com/PythonistaGuild/Wavelink) - A fully asynchronous Lavalink v4 wrapper built for discord.py.
- [devoxin/Lavalink.py](https://github.com/devoxin/Lavalink.py) - A powerful, intuitive Python wrapper for Lavalink.
- [cloudwithax/pomice](https://github.com/cloudwithax/pomice) - A modern Lavalink wrapper for discord.py with Spotify and Apple Music querying.
- [ooliver1/mafic](https://github.com/ooliver1/mafic) - A typed Lavalink client for discord.py and related forks.
- [PyLav/PyLav](https://github.com/PyLav/PyLav) - A Lavalink wrapper aimed at discord.py bots, including Red-DiscordBot.

### Authentication

- [treeben77/discord-oauth2.py](https://github.com/treeben77/discord-oauth2.py) - API Wrapper for Discord OAuth2 & Linked Roles in Python.
- [Soheab/oauthcord.py](https://github.com/Soheab/oauthcord.py) - An async Discord OAuth2 client with typed REST models. Not a bot framework.

### Metrics, Monitoring, and Logging

- [discord-ext-prometheus](https://github.com/ApolloRoboto/discord.py-ext-prometheus) - An extension for the discord.py library that enables Prometheus metrics.
- [loguru-discord](https://pypi.org/project/loguru-discord/) - Lightweight sink for Loguru that sends logs to Discord via webhook.

### Miscellaneous

- [Skelmis/Discord-Anti-Spam](https://github.com/Skelmis/Discord-Anti-Spam) - DPY Anti-Spam is a package aimed to handle all required logic under the hood for handling spammers.
- [YousefEZ/discord-qalib](https://github.com/YousefEZ/discord-qalib) - Discord library built on discord.py to simplify source code by rendering markup (xml) templates of embeds and menus (Pagination).
- [CasuallyCalm/discord-pretty-help](https://github.com/CasuallyCalm/discord-pretty-help) - An embed version of the built in help command for discord.py.
- [mahtoid/DiscordChatExporterPy](https://github.com/mahtoid/DiscordChatExporterPy) - Export Discord channel chats to HTML transcripts from a discord.py bot.
- [Bluenix2/discord-typings](https://github.com/Bluenix2/discord-typings) - TypedDict typings for Discord API payloads.

### Templates

- [kkrypt0nn/Python-Discord-Bot-Template](https://github.com/kkrypt0nn/Python-Discord-Bot-Template) - A simple, actively maintained template for starting a personalized discord.py bot.
- [PaulMarisOUMary/Discord-Bot](https://github.com/PaulMarisOUMary/Discord-Bot) - An advanced discord.py 2.x starter with hybrid commands, Docker, logging, and database support.

## Example Bots

- [Rapptz/RoboDanny](https://github.com/Rapptz/RoboDanny) - A Discord bot written by Rapptz, the creator of discord.py.
- [statch/gitbot](https://github.com/statch/gitbot) - GitBot is a programmer toolkit for developers to stay productive and connect with their friends on GitHub right from Discord.
- [python-discord/bot](https://github.com/python-discord/bot) - The community bot for the Python Discord community.
- [python-discord/metricity](https://github.com/python-discord/metricity) - Advanced metric collection for the Python Discord server.
- [alllthingslinux/tux](https://github.com/allthingslinux/tux) - Tux is an all in one bot for the All Things Linux Discord server.
- [DeJayDev/speedboat](https://github.com/DeJayDev/speedboat) - A Discord bot for managing large communities.
- [joinemm/miso-bot](https://github.com/joinemm/miso-bot) - Miso is a multipurpose Discord bot with over 100 commands and features.
- [AlexFlipnote/discord_bot](https://github.com/AlexFlipnote/discord_bot.py) - A simple Discord bot that helps you getting started within discord.py.
- [ZRunner/Axobot](https://github.com/Axobot-org/Axobot) - A cool multipurpose Discord bot made in Python.
- [MikeyUsersREC/ERM](https://github.com/MikeyUsersREC/ERM) - A Discord bot primarily focused on improving the Roblox staff experience.
- [Hunter87ff/Spruce](https://github.com/Hunter87ff/Spruce) - Spruce is a multi-functional open source Discord bot, designed to streamline the management of Discord tournaments and servers.
- [poketwo/poketwo](https://github.com/poketwo/poketwo) - A Pokémon-oriented Discord bot that lets you collect pokémon. Catch pokémon in the wild, level your pokémon, compete with your friends, and more.
- [wasi-master/wm_bot](https://github.com/wasi-master/wm_bot) - A multipurpose Discord bot with more than 220 commands.
- [DuckBot-Discord/DuckBot](https://github.com/DuckBot-Discord/DuckBot) - Source for DuckBot, a feature-rich discord.py bot with PostgreSQL and a documented local setup.
- [DTS-11/PizzaHat](https://github.com/DTS-11/PizzaHat) - A multi-purpose discord.py bot with a public website and AGPL source.
- [avizum/alpine](https://github.com/avizum/alpine) - A discord.py bot kept as a public reference implementation.
- [Nirlep5252/EpicBot](https://github.com/Nirlep5252/EpicBot) - A simple, multipurpose discord.py bot with a large public command set.
- [Kile/Killua](https://github.com/Kile/Killua) - Source for Killua, a maintained discord.py bot with extra algorithm notes in-tree.
- [Cog-Creators/Red-DiscordBot](https://github.com/Cog-Creators/Red-DiscordBot) - A modular, multi-function discord.py bot framework with a large cog ecosystem.
- [modmail-dev/Modmail](https://github.com/modmail-dev/Modmail) - A staff shared-inbox bot for Discord, similar to Reddit Modmail.
- [python-discord/sir-lancebot](https://github.com/python-discord/sir-lancebot) - Python Discord's community bot for newer open-source contributors.
- [ChocoMeow/Vocard](https://github.com/ChocoMeow/Vocard) - A user-friendly discord.py music bot with YouTube, SoundCloud, Spotify, and Twitch support.
- [cheran-senthil/TLE](https://github.com/cheran-senthil/TLE) - A discord.py bot for competitive programming on Codeforces and similar sites.
- [jakobdylanc/llmcord](https://github.com/jakobdylanc/llmcord) - A discord.py bot that turns Discord into a collaborative LLM frontend.
- [Ballsdex-Team/BallsDex-DiscordBot](https://github.com/Ballsdex-Team/BallsDex-DiscordBot) - Collect-and-trade countryballs bot written with discord.py.
- [onerandomusername/monty-python](https://github.com/onerandomusername/monty-python) - A discord.py bot for helping with Python project development.
- [AbstractUmbra/Mipha](https://github.com/AbstractUmbra/Mipha) - Umbra's personal discord.py bot, useful as a modern reference implementation.
- [PythonistaGuild/Pythonista-Bot](https://github.com/PythonistaGuild/Pythonista-Bot) - The discord.py bot for the Pythonista Guild server.
- [fourjr/rainbot](https://github.com/fourjr/rainbot) - A discord.py moderation bot with automod and logging.
- [Tortoise-Community/tortoise-bot](https://github.com/Tortoise-Community/tortoise-bot) - A fully featured discord.py community bot.

## Blog Posts, Guides and Tutorials

- [User Installable Applications - Umbra's Rantings](https://about.abstractumbra.dev/discord.py/2024/04/11/user-installable-applications.html) - This post is all about User Installable Applications and how to set them up.
- [All about selects - Umbra's Rantings](https://about.abstractumbra.dev/discord.py/2023/09/25/selects.html) - This post is about the different types of select menus and how to use them.
- [Application Command definition examples - Umbra's Rantings](https://about.abstractumbra.dev/discord.py/2023/01/30/app-command-examples.html) - This post is about the different types of application commands and how to use them.
- [Application command basics - Umbra's Rantings](https://about.abstractumbra.dev/discord.py/2023/01/30/app-command-basics.html) - In this guide, you'll cover everything from regular ol' slash commands all the way to Modals and the other component goodies.
- [Umbra's Sync Command - Umbra's Rantings](https://about.abstractumbra.dev/discord.py/2023/01/29/sync-command-example.html) - A full featured command and explanation for syncing your CommandTree.
- [Discord.py Masterclass](https://fallendeity.github.io/discord.py-masterclass/) - A tutorial/guide explaining all features in discord.py and how to make a Discord bot from scratch.
- [Python Discord - Discord.py Learning Guide](https://www.pythondiscord.com/pages/guides/python-guides/discordpy/) - A curated learning path covering bot setup, commands, FAQ, and commonly cited community examples.
- [Components V2 - Umbra's Rantings](https://about.abstractumbra.dev/discord.py/2025/08/17/components-v2.html) - Guide to discord.py 2.6 LayoutView and Discord's Components V2 system.

## Community Gists and Snippets

- [scragly/Learning discord.py](https://gist.github.com/scragly/095b5278a354d46e86f02d643fc3d64b) - Comprehensive guide and resource list for learning and building Discord bots using discord.py, including setup, essential concepts, and examples.
- [esmaycat/Message Components](https://gist.github.com/esmaycat/500eafdad0aaf278b94c612764688976) - This gist shows you how to use message components in discord.py 2.0.
- [advaith1/Intents Explainer](https://gist.github.com/advaith1/e69bcc1cdd6d0087322734451f15aa2f) - If you're wondering what Gateway Intents are, what Privileged Intents are, why your bot can't see statuses, or why your bot can't see member joins anymore, then this page should explain it to you!
- [cibere/Defer Response](https://gist.github.com/cibere/7e1356575780e716d2e3a23ea2bcf6da) - The defer response, defers the interaction response. This is typically used when the interaction is acknowledged and an optional secondary action will be done later. When deferring, you get up to 15 minutes to respond instead of the normal 3 seconds.
- [Jeftaei/AppCommandErrorhandler.py](https://gist.github.com/Jeftaei/d0bad5044f1192a4c454f95a6b591d53) - A robust error handler for discord.py commands, including app commands.
- [mikeshardmind/SQLite Examples](https://gist.github.com/mikeshardmind/d7d2c6cb19b53ab76b7d401b2716df5d) - "Common" Discord bot SQLite examples.
- [AkshuAgarwal/Interactions](https://gist.github.com/AkshuAgarwal/bc7d45bcecd5d29de4d6d7904e8b8bd8) - A Basic guide about Discord Interactions and how to use them in discord.py.
- [LeoCx1000/MentionableTree implementation](https://gist.github.com/LeoCx1000/021dc52981299b95ea7790416e4f5ca4) - Mentionable CommandTree implementation to allow mentioning slash commands in discord.py.
- [lykn/Buttons](https://gist.github.com/lykn/bac99b06d45ff8eed34c2220d86b6bf4) - A gist which shows/tells you how to make buttons using discord.py v2.
- [lykn/Selects or Dropdowns](https://gist.github.com/lykn/a2b68cb790d6dad8ecff75b2aa450f23) -  A gist explaining the right way to make drop down menus/select menus/selects in discord.py v2.
- [Ikusaba-san/Cog Methods](https://gist.github.com/Ikusaba-san/69115b79d33e05ed07ec4a4f14db83b1) - A list of all special cog methods.
- [Painezor/Checks](https://gist.github.com/Painezor/eb2519022cd2c907b56624105f94b190) - A list of built-in Checks for the commands extension of discord.py.
- [InterStella0/HelpCommand walkthrough](https://gist.github.com/InterStella0/b78488fb28cadf279dfd3164b9f0cf96) - Walkthrough for subclassing discord.py's HelpCommand.
- [Gobot1234/Sub-classing Help](https://gist.github.com/Gobot1234/45cad24df63fc144e85a7f8c85812567) - Guide to subclassing the help command in discord.py.
- [nonchris/Custom Help Command](https://gist.github.com/nonchris/1c7060a14a9d94e7929aa2ef14c41bc2) - An advanced custom help command example for discord.py bots.
- [voidoak/Implementing Help](https://gist.github.com/voidoak/4f34922888eeca04e1bba8c0ebd2f948) - Tutorial on implementing your own help command in discord.py.
- [Soheab/Simple Button Paginator](https://gist.github.com/Soheab/f226fc06a3468af01ea3168c95b30af8) - A small paginator with three buttons.
- [CuteFwan/wait_for Multiple Events](https://gist.github.com/CuteFwan/ded1bf520d71baac18726fa2e0554f0f) - Example of waiting for multiple Discord events.
- [Samarthh2601/App Commands Walkthrough](https://gist.github.com/Samarthh2601/b6f57065f394b54f43666037ade38d32) - Walkthrough for discord.py application commands.
- [imptype/Message Maker](https://gist.github.com/imptype/7b35c6769684fb68178e5719e5f81b6d) - An embed/message builder command for discord.py.
- [EvieePy/Cogs Example](https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be) - Classic cogs/extension layout example for discord.py rewrite.
- [EvieePy/Error Handling](https://gist.github.com/EvieePy/7822af90858ef65012ea500bcecf1612) - Error handling for prefix and app commands in discord.py.
- [Rapptz/Embed Help Command](https://gist.github.com/Rapptz/31a346ed1eb545ddeb0d451d81a60b3b) - Embed-based help command example from the discord.py author.
- [kkrypt0nn/ANSI Colors on Discord](https://gist.github.com/kkrypt0nn/a02506f3712ff2d1c8ca7c9e0aed7c06) - Guide to ANSI color codes in Discord code blocks.
- [LeviSnoot/Discord Timestamps](https://gist.github.com/LeviSnoot/d9147767abeef2f770e9ddcd91eb85aa) - Discord timestamp markdown syntax reference.
- [InterStella0/Pagination Walkthrough](https://gist.github.com/InterStella0/454cc51e05e60e63b81ea2e8490ef140) - Walkthrough of action-based pagination in discord.py.
- [mikeshardmind/List Menu](https://gist.github.com/mikeshardmind/bff6f937032455d83b8f1724ef73575a) - List menu pagination snippet for discord.py.
- [irregularunit/Command Error Handler](https://gist.github.com/irregularunit/0221164777a476c653e36b49439b7b06) - Structured command error handler example for discord.py.
- [4Kaylum/Discord.py Tutorial](https://gist.github.com/4Kaylum/a1e9f31c31b17386c36f017d3c59cdcc) - A simple bot tutorial for discord.py.
- [quackbarc/2.0 Paginators](https://gist.github.com/quackbarc/31e5cd789d232ad0d263511bb1a506e8) - Paginator examples for discord.py 2.0.
- [philskillz-coder/Color Transformer](https://gist.github.com/philskillz-coder/c6bee6c8e258ad56afb01840df26a1fa) - Color transformer and autocomplete for discord.py.
- [Soheab/Components V2 to LayoutView](https://gist.github.com/Soheab/ab7a833725f95a84a8f7fa17995cb36c) - Example of mapping Discord Components V2 to discord.py LayoutView.
- [Soheab/CV2 Paginator](https://gist.github.com/Soheab/891c39d7294b1bdbadc7ecf35ce51cc5) - A Components V2 paginator for discord.py.
- [Soheab/Threads](https://gist.github.com/Soheab/4709e335474784d8a1877812f6d0c354) - Guide to Discord threads and how to manage them with discord.py.
- [Soheab/Voice Channel Status](https://gist.github.com/Soheab/e9a747f5c8fae43447a5611e483b4beb) - How to react when a voice channel status is set or changed.
- [Soheab/No Message Content Intent Ideas](https://gist.github.com/Soheab/a6229dbbe3acf3ce9a4625bf9e7177da) - Command ideas that work without the privileged message content intent.
- [Soheab/Embed to Container](https://gist.github.com/Soheab/cf356c62a6134508869bf40640b04856) - Convert a discord.py embed into a Components V2 container.
- [Soheab/self.bot in Cogs](https://gist.github.com/Soheab/cf387b753da32eb02f3228c2e32bb03f) - Explains how `self.bot` works inside a discord.py cog.
- [Soheab/wait_for Modal](https://gist.github.com/Soheab/f46fee27498aad4a8962d59b6f0415c6) - Wait for user input with a modal in discord.py.
- [Soheab/wait_for in Commands](https://gist.github.com/Soheab/e73ab6f66881ee4102be37815da3a24e) - Examples of `wait_for` inside ext.commands.
- [Soheab/Global View](https://gist.github.com/Soheab/cfd769870b7b6eaf00a7aebf5293a622) - Pattern for a globally registered discord.py view.
- [Soheab/Any-Permission Check](https://gist.github.com/Soheab/ec3f40f9f54add0dba787783719331f8) - A custom check that passes if the user has any of the given permissions.
- [Soheab/discord.Colour](https://gist.github.com/Soheab/d9cf3f40e34037cfa544f464fc7d919e) - Reference for discord.Colour helpers and usage.
- [Soheab/APIs for Discord Bots](https://gist.github.com/Soheab/332ba85f8989648449c71bdc8ef32368) - Community list of APIs commonly used with Discord bots.

## Additional Resources

- [Permissions Calculator](https://discordapi.com/permissions.html) - Create invite links for bots with specific permissions.
- [Discord Community Resources](https://discord.com/developers/docs/topics/community-resources) - Official Discord docs index of libraries, permission/intent calculators, and embed tools.
- [Intent Calculator](https://ziad87.net/intents/) - Build a gateway intents bitfield for your Identify payload.
- [Embed Visualizer](https://leovoel.github.io/embed-visualizer/) - Live Discord embed designer with generated library snippets.
- [discord-interactions-python](https://github.com/discord/discord-interactions-python) - Official Discord helpers for verifying HTTP interaction signatures in Python.
- [awesome-discord-communities](https://github.com/mhxion/awesome-discord-communities) - A curated list of Discord communities for programmers.
- [jacc/awesome-discord](https://github.com/jacc/awesome-discord) - A curated list of Discord clients, bots, libraries, and related tools.
- [Discord Library Comparison](https://libs.advaith.io) - Compares Discord libraries and their support for current API features.
- [Soheab/dpy-missing-features](https://github.com/Soheab/dpy-missing-features) - Notes on Discord API features that discord.py does not (yet) expose.
- [Soheab/discord.py-tags](https://github.com/Soheab/discord.py-tags) - Overflow copies of long tags from the official discord.py Discord server.
- [Soheab/dpy-badhosts](https://github.com/Soheab/dpy-badhosts) - Hosts the discord.py community generally warns against using for bots.

## Forks and Wrappers

- [disnake](https://github.com/DisnakeDev/disnake) - A modern, easy to use, feature-rich, and async-ready API wrapper for Discord written in Python.
- [nextcord](https://github.com/nextcord/nextcord) - A Python wrapper for the Discord API forked from discord.py.
- [Novus](https://github.com/Voxel-Fox-Ltd/Novus) - An asyncio Python wrapper around the Discord API, forked off of Rapptz's Discord.py.
- [pycord](https://github.com/Pycord-Development/pycord) - A maintained fork of discord.py that wraps the Discord API.
- [mccoderpy/discord.py-message-components](https://github.com/mccoderpy/discord.py-message-components) - A "fork" of discord.py library made by Rapptz with implementation of the Discord Message-Components & many other features by mccoderpy.
- [tibue99/ezcord](https://github.com/tibue99/ezcord) - An easy-to-use extension for Discord.py and Pycord.
- [hikari](https://github.com/hikari-py/hikari) - A Discord API wrapper for Python and asyncio, built independently of discord.py.
- [interactions.py](https://github.com/interactions-py/interactions.py) - A highly extensible Discord bot framework for Python.
- [hata](https://github.com/HuyaneMatsu/hata) - An async Discord API wrapper for Python, independent of discord.py.
- [AlexFlipnote/discord.http](https://github.com/AlexFlipnote/discord.http) - An HTTP-interactions-first Discord library with optional gateway support.

## Archived/Deprecated

- [thrzl/discord-ext-forms](https://github.com/thrzl/discord-ext-forms) - A simpler way to make forms, surveys, and reaction input using discord.py.
- [Ext-Creators/discord-ext-events](https://github.com/Ext-Creators/discord-ext-events) - A discord.py extension with additional events.
- [Ext-Creators/discord-ext-converters](https://github.com/Ext-Creators/discord-ext-converters) - A discord.py extension with a collection of useful converters.
- [Ext-Creators/discord-ext-rx](https://github.com/Ext-Creators/discord-ext-rx) - A discord.py extension with a reactive events implementation.
- [discord-py-ui/discord-ui](https://github.com/discord-py-ui/discord-ui) - A discord.py extension that allows you to create and manage buttons, slash commands, and more.
- [PythonistaGuild/buttons](https://github.com/PythonistaGuild/buttons) - Archived interactive session and reaction-button paginator for discord.py.
- [soosBot-com/Pagination](https://github.com/soosBot-com/Pagination) - Archived embed paginator library for discord.py 2.0.
- [Ext-Creators/discord-ext-ipc](https://github.com/Ext-Creators/discord-ext-ipc) - Archived discord.py IPC extension. Prefer better-ipc or discord-ext-ipcx.
- [EQUENOS/dislash.py](https://github.com/EQUENOS/dislash.py) - Archived slash-command and button wrapper from before discord.py 2.0.
- [woohyunjng/discord.py-components](https://github.com/woohyunjng/discord.py-components) - Archived unofficial components library from before native discord.py UI.
- [Ext-Creators/discord-ext-alternatives](https://github.com/Ext-Creators/discord-ext-alternatives) - Archived discord.py extension with extra and alternative features.
- [discordsuperutils/discord-super-utils](https://github.com/discordsuperutils/discord-super-utils) - Archived high-level helpers for common discord.py bot features.
- [XuaTheGrate/slash_util](https://github.com/XuaTheGrate/slash_util) - Archived helper for adding application commands on early discord.py 2.0.

<!-- END CONTENT -->

## Contributing

[Contributions of any kind welcome, just follow the guidelines](contributing.md)!

### Contributors

[Thanks goes to these contributors](https://github.com/kzndotsh/awesome-discordpy/graphs/contributors)!
