# MCDR-plugins
A plugin library for [MCDReforged](https://github.com/Fallen-Breath/MCDReforged).  
My own lightweight plugin.  
## Installation
place ``run_some_commands_v1.0.0.mcdr`` in the ``./plugins`` folder.  
## Config
After the plugin is loaded, ``rsc.config`` should be created in the ``./config`` folder.  
Or you can create it manually.  
``
{"0":[],"1":[],"2":[],"3":[],"4":[]}
``

## Commands
```
!!rsc - Show help message
!!rsc <command> [<params>] - execute vanilla command  
!!rsclist - list all the commands that had been added into the whitelist  
!!rscadd <command> <permission> - add the command into the whitelist  
!!rscrem <command> - remove the command from the whitelist  
P/S: The permission in the !!rscadd should be the highest permission value for the command that can be executed by.  
```
# MCDR-plugins
一個 [MCDReforged](https://github.com/Fallen-Breath/MCDReforged) 的插件庫  
我自己製作的輕量級插件  
## 安裝
將 ``run_some_commands_v1.0.0.mcdr`` 放置在 ``./plugins`` 資料夾裡.  
## Config
加載插件后, ``rsc.config`` 將自動被生成于 ``./config`` 資料夾裡  
你也可以手動生成   
``
{"0":[],"1":[],"2":[],"3":[],"4":[]}
``

## 指令
```
!!rsc - 顯示這條消息  
!!rsc <原版指令> [<參數>] - 執行原版指令  
!!rsclist - 顯示所有已被添加至白名單的指令  
!!rscadd <原版指令> <權限> - 添加指令至白名單  
!!rscrem <原版指令> - 從白名單中移除指令  
P/S: 請在設置權限時將權限設爲最高可執行此指令的權限代號  
```
