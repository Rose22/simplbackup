# simplbackup
lightweight python script that quickly takes a bunch of folders from all over your system and compresses them all into one neat packaged zip that can be exactly defined the way you want it. great for tidy backups!

it works by defining a file like this:

```
emulation_saves.{date}.zip

/home/user/.retroarch/saves/ : emulation/saves/retroarch
/home/user/.config/dolphin/GC/ : emulation/saves/dolphin/GC
/home/user/.config/dolphin/Wii/ : emulation/saves/dolphin/Wii
/home/user/.config/yuzu/nand/user/save : emulation/saves/yuzu
```

and so on.

this results in a file called `emulation_saves.08-08-2023.zip` that has the following file structure in it:
```
emulation/
  saves/
    retroarch/
    dolphin/
      GC/
      Wii/
    yuzu/
```

with those all containing the files from the source folders stated in the definition file.

as you can see, very useful for backing up emulation saves!
