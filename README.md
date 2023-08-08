# simplbackup
lightweight python script that quickly takes a bunch of folders from all over your system and compresses them all into one neat packaged zip that can be exactly defined the way you want it. great for tidy backups!

it works by defining a file like this:

```
emulation_saves.{date}.zip

/home/user/.retroarch/saves/ : saves/retroarch
/home/user/.config/dolphin/GC/ : saves/dolphin/GC
/home/user/.config/dolphin/Wii/ : saves/dolphin/Wii
/home/user/.config/yuzu/nand/user/save : saves/yuzu
```

and so on.

you save that as something like "emubackup.conf". 

then run `simplbackup emubackup.conf`

this results in a file called `emulation_saves.08-08-2023.zip` that has the following file structure in it:
```
saves/
  retroarch/
    ..all the retroarch files..
  dolphin/
    GC/
      USA/
        Card A/
          ..all the files..
      EUR/
      JAP/
    Wii/
      ..all the wii files..
  yuzu/
    ..all the yuzu saves..
```

with those all containing the files from the source folders stated in the definition file.

as you can see, very useful for backing up emulation saves!
