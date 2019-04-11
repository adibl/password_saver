#############################################################################
# Generated by PAGE version 4.22
#  in conjunction with Tcl version 8.6
#  Apr 11, 2019 04:00:07 PM +0300  platform: Windows NT
set vTcl(timestamp) ""


if {!$vTcl(borrow)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(active_menu_fg) #000000
}

#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top42
    global vTcl
    set base $vTcl(btop)
    if {$base == ""} {
        set base .top42
    }
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# GENERATED GUI PROCEDURES
#
    menu .pop47 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -font {-family {Segoe UI} -size 9} \
        -foreground black -tearoff 1 
    vTcl:DefineAlias ".pop47" "Popupmenu1" vTcl:WidgetProc "" 1
    menu .pop48 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -font {-family {Segoe UI} -size 9} \
        -foreground black -tearoff 1 
    vTcl:DefineAlias ".pop48" "Popupmenu2" vTcl:WidgetProc "" 1
    menu .pop49 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -font {-family {Segoe UI} -size 9} \
        -foreground black -tearoff 1 
    vTcl:DefineAlias ".pop49" "Popupmenu3" vTcl:WidgetProc "" 1

proc vTclWindow.top42 {base} {
    if {$base == ""} {
        set base .top42
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m50" -background {#d9d9d9} -highlightbackground {#d9d9d9} \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 296x261+585+210
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1684 1031
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    button $top.but43 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -command {self.run,command= self.parse} \
        -disabledforeground {#a3a3a3} -font TkDefaultFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text Register 
    vTcl:DefineAlias "$top.but43" "Button1" vTcl:WidgetProc "Toplevel1" 1
    bind $top.but43 <Enter> {
        self.run
    }
    entry $top.ent44 \
        -background white -disabledforeground {#a3a3a3} \
        -font {-family {Courier New} -size 10} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -selectbackground {#c4c4c4} \
        -selectforeground black -textvariable entity_username 
    vTcl:DefineAlias "$top.ent44" "entry_username" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.m50
    menu $site_3_0 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -font {-family {Segoe UI} -size 9} \
        -foreground {#000000} -tearoff 0 
    spinbox $top.spi51 \
        -activebackground {#f9f9f9} -background white \
        -buttonbackground {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font {-family {Segoe UI} -size 9} -foreground black -from 1.0 \
        -highlightbackground black -highlightcolor black -increment 1.0 \
        -insertbackground black -selectbackground {#c4c4c4} \
        -selectforeground black -textvariable spinbox_question -to 100.0 \
        -values {1 2 6 79 {}} 
    vTcl:DefineAlias "$top.spi51" "Spinbox_question" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab54 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Username 
    vTcl:DefineAlias "$top.lab54" "Label1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab55 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Password 
    vTcl:DefineAlias "$top.lab55" "Label2" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent57 \
        -background white -disabledforeground {#a3a3a3} \
        -font {-family {Courier New} -size 10} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -selectbackground {#c4c4c4} \
        -selectforeground black -textvariable entitiy_password 
    vTcl:DefineAlias "$top.ent57" "entry_password" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab58 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Quiestion 
    vTcl:DefineAlias "$top.lab58" "Label3" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent60 \
        -background white -disabledforeground {#a3a3a3} \
        -font {-family {Courier New} -size 10} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -selectbackground {#c4c4c4} \
        -selectforeground black -textvariable entity_answer 
    vTcl:DefineAlias "$top.ent60" "entry_aswer" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab61 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Answer 
    vTcl:DefineAlias "$top.lab61" "Label4" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab43 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text { } 
    vTcl:DefineAlias "$top.lab43" "lable_answer_error" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab44 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text { } 
    vTcl:DefineAlias "$top.lab44" "lable_question_error" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab45 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text { } 
    vTcl:DefineAlias "$top.lab45" "lable_password_error" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab46 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text { } 
    vTcl:DefineAlias "$top.lab46" "lable_username_error" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.but43 \
        -in $top -x 100 -y 210 -width 87 -relwidth 0 -height 24 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent44 \
        -in $top -x 90 -y 40 -anchor nw -bordermode ignore 
    place $top.spi51 \
        -in $top -x 90 -y 120 -width 165 -relwidth 0 -height 19 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab54 \
        -in $top -x 10 -y 40 -width 74 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab55 \
        -in $top -x 10 -y 80 -width 74 -height 21 -anchor nw \
        -bordermode ignore 
    place $top.ent57 \
        -in $top -x 90 -y 80 -width 164 -height 20 -anchor nw \
        -bordermode ignore 
    place $top.lab58 \
        -in $top -x 10 -y 120 -width 74 -height 21 -anchor nw \
        -bordermode ignore 
    place $top.ent60 \
        -in $top -x 90 -y 160 -width 164 -height 20 -anchor nw \
        -bordermode ignore 
    place $top.lab61 \
        -in $top -x 10 -y 160 -width 74 -height 21 -anchor nw \
        -bordermode ignore 
    place $top.lab43 \
        -in $top -x 90 -y 180 -width 164 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab44 \
        -in $top -x 90 -y 140 -width 164 -height 21 -anchor nw \
        -bordermode ignore 
    place $top.lab45 \
        -in $top -x 90 -y 100 -width 164 -height 21 -anchor nw \
        -bordermode ignore 
    place $top.lab46 \
        -in $top -x 90 -y 60 -width 164 -height 21 -anchor nw \
        -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top42 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

