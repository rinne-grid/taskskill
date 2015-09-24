task_ymd = $("#datepicker_task_ymd").val()



if task_ymd is "undefined"
    today = new Date()
    year = today.getFullYear()
    month = ("0"+(today.getMonth()+1)).slice(-2)
    day = ("0"+today.getDate()).slice(-2)
    console.log today.getDate()

    task_ymd = "#{year}-#{month}-#{day}"

$("#datepicker").datepicker(
    {
        dateFormat: "yy-mm-dd",
    }
).val(task_ymd)




###
    メモ登録ボタンクリック時の処理
###
$(document).on "click", ".list-item-edit", ->
    task_id = $(this).parent().find('.user_task_id').val()
    task_memo = $(this).parent().find('.task_memo').val()
    console.log(task_memo)

    #that = this
    add_user_task_memo(task_id, task_memo)

    return

###
    タスク削除ボタンクリック時の処理
###
$(document).on "click", ".list-item-delete", ->
    task_id = $(this).parent().find('.user_task_id').val()
    console.log task_id

    that = this
    # TODO: 削除確認用のメッセージを表示する
    del_user_task(task_id, that)

    return

###
    終了チェック時の処理
###
$(document).on 'change', '.finish_check', ->
    task_id = $(this).parent().find('.user_task_id').val()
    status = "doing"
    if $(this).is(':checked') is true
        status = "finished"
    that = this
    do_user_task_status(task_id, status, that)
    return
#alert(status)

###
    タスク項目クリック時の処理
###
$(document).on "click", ".list-item", ->
    target_task_id = $(this).find('input').val()

    task_item_name = $(this).html()
    # AjaxでDBタスクに登録
    loading(true)
    cre_user_task(target_task_id, task_item_name)
    return


###
    loadingを表示を制御する
###
loading = (bool) ->
    if bool is true
        $(".loading").css('display', 'block')
    else
        $(".loading").css('display', 'none')
    return

window.loading = loading;



