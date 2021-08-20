import json
import os

Prefix = "!!rsc"
help_msg = \
"""
----------RSC----------
§7!!rsc §r- §b顯示這條消息
§7!!rsc <原版指令> [<參數>] §r- §b執行原版指令
§7!!rsclist §r- §b顯示所有已被添加至白名單的指令
§7!!rscadd <原版指令> <權限> §r- §b添加指令至白名單
§7!!rscrem <原版指令> §r- §b從白名單中移除指令
§cP/S: 請在設置權限時將權限設爲最高可執行此指令的權限代號
"""
permission_list = {"0":"guest","1":"user","2":"helper","3":"admin","4":"owner"}

PLUGIN_METADATA = {
     'id': 'run_some_commands',
     'version': '1.0.0',
     'name': 'Run some commands',
     'author': 'FlyingShuriken',
     'link': 'https://github.com/FlyingShuriken/MCDR-plugins'
}

CONFIG_FILE = './config/rsc.json'

def on_user_info(server, info):
    if info.content == "!!rsc":
        server.tell(info.player,help_msg)
        return
    elif info.content == "!!rsclist":
        with open(CONFIG_FILE,"r") as cfg:
            perm = json.load(cfg)
        all_cmd = ""
        for i in perm:
            all_cmd += f"§e{permission_list[i]} - §b{str(perm[i])}\n"
        server.tell(info.player, all_cmd)
    else:
        cmd = info.content.split(" ")
        if cmd[0] == "!!rscadd":
            if server.get_permission_level(info.player) == 4:
                with open(CONFIG_FILE,"r") as cfg:
                    perm = json.load(cfg)
                perm[cmd[2]].append(cmd[1])
                open(CONFIG_FILE,"w").write(json.dumps(perm))
                server.tell(info.player, f"§c此指令已被添加至 §9{permission_list[cmd[2]]}§c或以下的權限")
                return
            else:
                server.tell(info.player, f"§c此指令只能由具owner權限之玩家使用")
                return
        elif cmd[0] == "!!rscrem":
            if server.get_permission_level(info.player) == 4:
                with open(CONFIG_FILE,"r") as cfg:
                    perm = json.load(cfg)
                perm[cmd[2]].remove(cmd[1])
                open(CONFIG_FILE,"w").write(json.dumps(perm))
                server.tell(info.player, f"§c此指令已被移除")
                return
            else:
                server.tell(info.player, f"§c此指令只能由具owner權限之玩家使用")
                return
        elif cmd[0] == "!!rsc":
            prm_lvl = server.get_permission_level(info.player)
            with open(CONFIG_FILE,"r") as cfg:
                perm = json.load(cfg)
            executable = []
            for i in range(prm_lvl+1):
                executable.extend(perm[str(i)])
            if cmd[1] in executable:
                cmd.remove("!!rsc")
                params = ""
                for i in cmd:
                    params += f"{i} "
                command = f"execute as {info.player} run {params}"[:-1]
                server.logger.info(command)
                server.execute(command)
            else:
                server.tell(info.player, "§c你沒有足夠的權限運行此指令, 或是此指令并沒有被添加至你的權限的指令白名單")
                return

def on_load(server, old):
    server.register_help_message("!!rsc","運行白名單指令")
    if "rsc.json" not in os.listdir("./config"):
        open(CONFIG_FILE,"w").write('{"0":[],"1":[],"2":[],"3":[],"4":[]}')
