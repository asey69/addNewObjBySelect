# Copyright 2019 Oleksii Zinchenko. All rights reserved.
# Tool for create the new object by selection.

import maya.cmds as cmds
import re


def AddNewObjBySelectUI():
    if (cmds.window('AddNewObjBySelect', query=True, exists=True)):
        cmds.deleteUI('AddNewObjBySelect', window=True)
    anoWindow = cmds.window('AddNewObjBySelect', t='Add new obj by select', s=0)
    anoCase = cmds.rowColumnLayout('inoCase', nc=1, cal=[(1, 'left')], rs=[(1, 5)], cs=[(1, 0)], cw=[(1, 325)],
                                   p=anoWindow)
    anoObjOptionBlock = cmds.rowColumnLayout('anoObjOptionBlock', nc=5,
                                             cal=[(1, 'left'), (2, 'left'), (3, 'left'), (4, 'right'), (5, 'left')],
                                             rs=[(1, 5), (2, 5), (3, 5), (4, 5), (5, 5)],
                                             cs=[(1, 5), (2, 5), (3, 5), (4, 5), (5, 5)],
                                             cw=[(1, 65), (2, 65), (3, 65), (4, 80), (5, 20)],
                                             p=anoCase)
    cmds.radioCollection('anoObjType_rCollection', p=anoObjOptionBlock)
    for a in ['group', 'locator', 'joint']:
        cmds.radioButton((a + '_rButton'), l=a)
    cmds.text(l='use namespace:', p=anoObjOptionBlock)
    cmds.checkBox('use_ns', v=0, p=anoObjOptionBlock)
    cmds.separator(p=anoCase)
    anoCutNameBlock = cmds.rowColumnLayout('anoCutNameBlock', nc=5,
                                           cal=[(1, 'right'), (2, 'left'), (3, 'right'), (4, 'left'), (5, 'left')],
                                           rs=[(1, 0), (2, 0), (3, 0), (4, 0), (5, 0)],
                                           cs=[(1, 0), (2, 5), (3, 5), (4, 5), (5, 5)],
                                           cw=[(1, 60), (2, 85), (3, 50), (4, 85), (5, 20)],
                                           p=anoCase)
    cmds.text(l='startCut:', p=anoCutNameBlock)
    cmds.textField('anoStartCut_txtField', ed=True, tx='',
                   ann='set how many symbols to cut off at the beginning of the name of the selected object',
                   p=anoCutNameBlock)
    cmds.text(l='endCut:', p=anoCutNameBlock)
    cmds.textField('anoEndCut_txtField', ed=True, tx='',
                   ann='set how many symbols to cut off at the ending of the name of the selected object',
                   p=anoCutNameBlock)
    cmds.button('clearCut_btn', l='x', c='anoClear(\'cut\')', p=anoCutNameBlock)
    cmds.separator(p=anoCase)
    anoNewNameBlock = cmds.rowColumnLayout('anoNewNameBlock', nc=6,
                                           cal=[(1, 'left'), (2, 'left'), (3, 'left'), (4, 'left'), (5, 'left'),
                                                (6, 'left')],
                                           rs=[(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)],
                                           cs=[(1, 0), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5)],
                                           cw=[(1, 45), (2, 30), (3, 135), (4, 5), (5, 60), (6, 20)],
                                           p=anoCase)
    cmds.textField('anoPref_txtField', ed=True, tx='', ann='set prefix of the new object', p=anoNewNameBlock)
    cmds.text(l='_root_', p=anoNewNameBlock)
    cmds.textField('anoIdent_txtField', ed=True, tx='', ann='set identificator of the new object', p=anoNewNameBlock)
    cmds.text(l='_', p=anoNewNameBlock)
    cmds.textField('anoSuff_txtField', ed=True, tx='', ann='set suffix of the new object', p=anoNewNameBlock)
    cmds.button('clearName_btn', l='x', c='anoClear(\'name\')', p=anoNewNameBlock)
    cmds.separator(p=anoCase)
    anoButtonBlock = cmds.rowColumnLayout('anoButtonBlock', nc=5,
                                          cal=[(1, 'left'), (2, 'left'), (3, 'left'), (4, 'left'), (5, 'left')],
                                          rs=[(1, 0), (2, 0), (3, 0), (4, 0), (5, 0)],
                                          cs=[(1, 0), (2, 5), (3, 5), (4, 5), (5, 5)],
                                          cw=[(1, 60), (2, 60), (3, 60), (4, 60), (5, 60)],
                                          p=anoCase)
    for a in [['AddUp', 'add before', 'anoAddNewObj(0)', 'add the new object before selection object'],
              ['AddDn', 'add after', 'anoAddNewObj(1)', 'add the new object under selection object'],
              ['AddBeside', 'add beside', 'anoAddNewObj(2)', 'add the new object beside selection object'],
              ['AddBy', 'add by', 'anoAddNewObj(3)', 'add the new object by selection object'],
              ['AddNew', 'new', 'anoAddNewObj(4)', 'can be use multiselection']]:
        cmds.button((a[0] + '_btn'), l=a[1], c=a[2], ann=a[3], p=anoButtonBlock)

    cmds.showWindow(anoWindow)
    cmds.window('AddNewObjBySelect', e=True, wh=[325, 138])
    cmds.radioCollection('anoObjType_rCollection', e=True, sl='group_rButton')


def anoClear(t):
    if t == 'cut':
        n = 'anoCutNameBlock'
    else:
        n = 'anoNewNameBlock'

    l = cmds.rowColumnLayout(n, q=True, ca=True)
    for a in l:
        if re.findall('_txtField', a):
            cmds.textField(a, e=True, tx='')


def get_name(a, cutStart, cutEnd, pref, ident, num, suff, type):
    if a:
        if type == 4:
            a = ''
        else:
            if cutStart and cutEnd:
                a = a[cutStart:cutEnd * (-1)]
            elif cutStart and not cutEnd:
                a = a[cutStart:]
            elif not cutStart and cutEnd:
                a = a[:cutEnd * (-1)]

    if pref:
        if (type != 4 and a) or (type == 4 and (ident or num or suff)):
            pref = ('%s_' % pref)

    if ident and a:
        ident = ('_%s' % ident)

    if num and (a or ident):
        num = ('_%s' % num)

    if suff and (a or ident or num):
        suff = ('_%s' % suff)

    return ('%s%s%s%s%s' % (pref, a, ident, num, suff))


def add_object(name, objtype, a):
    cmds.select(cl=True)
    if objtype == 'group':
        cmds.group(em=True, n=name)
    elif objtype == 'locator':
        cmds.spaceLocator(n=name)
    elif objtype == 'joint':
        cmds.joint(n=name)

    cmds.parentConstraint(a, name, n='helpCon')
    cmds.delete('helpCon')


def anoAddNewObj(type):
    objtype = cmds.radioCollection('anoObjType_rCollection', q=True, sl=True)[:-8]
    ident = cmds.textField('anoIdent_txtField', q=True, tx=True)
    pref = cmds.textField('anoPref_txtField', q=True, tx=True)
    suff = cmds.textField('anoSuff_txtField', q=True, tx=True)
    use_namespace = cmds.checkBox('use_ns', q=True, v=True)

    if cmds.textField('anoStartCut_txtField', q=True, tx=True):
        cutStart = int(cmds.textField('anoStartCut_txtField', q=True, tx=True))
    else:
        cutStart = 0

    if cmds.textField('anoEndCut_txtField', q=True, tx=True):
        cutEnd = int(cmds.textField('anoEndCut_txtField', q=True, tx=True))
    else:
        cutEnd = 0

    t = cmds.ls(sl=True, fl=True)
    if t:
        if type == 4:
            if not pref and not ident and not suff:
                cmds.warning('// Warning! Please fill name UI and try agane!')
            else:
                num = ''
                for i in range(0, len(t), 1):
                    if len(t) > 1:
                        if len(str(i)) == len(str(len(t) - 1)):
                            num = str(i)
                        else:
                            num = str(i)
                            for n in range(0, (len(str(len(t) - 1)) - 1), 1):
                                num = ('0%s' % num)

                    tmp = t[i].split('|')[-1]
                    ns = tmp[:((len(t[0].split(':')[-1]) + 1) * (-1))]
                    root = tmp.split(':')[-1]
                    name = get_name(root, cutStart, cutEnd, pref, ident, num, suff, type)
                    if use_namespace and type != 4:
                        name = ('%s:%s' % (ns, name))

                    if cmds.objExists(name):
                        cmds.warning('// Warning! Object %s really exists!' % name)
                    else:
                        add_object(name, objtype, t[i])
        else:
            for a in t:
                tmp = a.split('|')[-1]
                ns = tmp[:((len(t[0].split(':')[-1]) + 1) * (-1))]
                root = tmp.split(':')[-1]
                name = get_name(root, cutStart, cutEnd, pref, ident, '', suff, type)
                if use_namespace:
                    name = ('%s:%s' % (ns, name))

                if cmds.objExists(name):
                    cmds.warning('// Warning! Object %s really exists!' % name)
                else:
                    if not type or type == 1:
                        ref = 0

                        if type:
                            p = cmds.listRelatives(a, p=False, c=True, f=True, typ='transform')
                            if p:
                                if cmds.referenceQuery(p[0], inr=True):
                                    ref += 1
                        else:
                            p = cmds.listRelatives(a, p=True, c=False, f=True, typ='transform')
                            if p:
                                if cmds.referenceQuery(p[0], inr=True):
                                    ref += 1

                        if ref:
                            cmds.warning('// Warning! Object %s is referenced and can not be reparented!' % name)
                        else:
                            add_object(name, objtype, a)
                    else:
                        add_object(name, objtype, a)

                    if cmds.objExists(name):
                        if type == 0 or type == 2:
                            p = cmds.listRelatives(a, p=True, c=False, f=True, typ='transform')
                            if p:
                                cmds.parent(name, p[0])
                            if type == 0:
                                cmds.parent(a, name)
                        if type == 1:
                            p = cmds.listRelatives(a, c=True, p=False, f=True, typ='transform')
                            if p:
                                for c in p:
                                    cmds.parent(c, name)
                            cmds.parent(name, a)
    else:
        cmds.warning('// Warning! Nothing selected!')


AddNewObjBySelectUI()
