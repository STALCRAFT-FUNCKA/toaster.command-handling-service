from .commands import (
    MarkCommand,
    PermissionCommand,
    GameCommand,
    SayCommand,
    DeleteCommand,
    CopyCommand,
    SettingsCommand,
    DelayCommand,
    KickCommand,
    AddCurseWordCommand,
    AddURLFilterPatternCommand,
    ExpireCommand,
    WarnCommand,
    PunishmentCommand,
    ProfileCommand,
    UnwarnCommand,
)


command_list = {
    PermissionCommand.NAME: PermissionCommand,
    MarkCommand.NAME: MarkCommand,
    GameCommand.NAME: GameCommand,
    SayCommand.NAME: SayCommand,
    DeleteCommand.NAME: DeleteCommand,
    CopyCommand.NAME: CopyCommand,
    SettingsCommand.NAME: SettingsCommand,
    DelayCommand.NAME: DelayCommand,
    KickCommand.NAME: KickCommand,
    AddCurseWordCommand.NAME: AddCurseWordCommand,
    AddURLFilterPatternCommand.NAME: AddURLFilterPatternCommand,
    ExpireCommand.NAME: ExpireCommand,
    WarnCommand.NAME: WarnCommand,
    PunishmentCommand.NAME: PunishmentCommand,
    ProfileCommand.NAME: ProfileCommand,
    UnwarnCommand.NAME: UnwarnCommand,
}


__all__ = ("command_list",)
