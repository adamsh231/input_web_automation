def loginSimpeg(driver, username, password):
    driver.get("http://simpeg.malangkota.go.id/index.php/login")
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_css_selector("button.btn.blue.pull-right").click()


def tambahJabatanByNIP(time, driver, nip, id="", id_so="", id_uniti="", id_unitk="", id_sub_unitk="", id_pejabat="", id_posisi=""):
    driver.get("http://simpeg.malangkota.go.id/index.php/informasi/pegawai")
    driver.find_element_by_id("nip_baru").send_keys(nip)
    driver.find_element_by_id("search_button").click()
    # driver.find_element_by_xpath('//*[@id="search_button"]').click()
    time.sleep(4)
    driver.find_element_by_xpath(
        '//*[@id="datatable_ajax"]/tbody/tr/td[5]/a[2]').click()
    driver.find_element_by_partial_link_text('Jabatan').click()
    driver.find_element_by_partial_link_text('Tambah').click()
    id = 3  # 3->pelaksana
    id_so = 6  # 6->2020
    id_uniti = 3  # 3->Dinas
    id_unitk = 3130  # 3130->Dinas Lingkungan Hidup
    id_sub_unitk = 1298  # 1298->UPT Pengelolaan Taman
    id_pejabat = 16  # 16->Sekretaris Daerah
    id_posisi = 29507  # 29507->Pramu Kebersihan Seksi Pengurangan
    tambahJabatanByNIP_extend(
        driver, id, id_so, id_uniti, id_unitk, id_sub_unitk, id_pejabat, id_posisi)


def tambahJabatanByNIP_extend(driver, id, id_so, id_uniti, id_unitk, id_sub_unitk, id_pejabat, id_posisi):
    console = list()
    console.append('$("#jenis_jabatan").select2("val", ' + str(id) + ');')
    console.append('$("#pejabat").select2("val", '+str(id_pejabat)+');')
    console.append(
        'document.getElementsByName("ket_pejabat")[0].value = "Sekretaris Daerah Kota Malang";')
    console.append('document.getElementById("tanggal_sk").value = "31122019";')
    console.append('document.getElementById("tmt_sk").value = "31122019";')
    console.append(
        'document.getElementById("atasan_pp").value = '+str(id_posisi)+';')
    console.append('$.ajax({url: "http://simpeg.malangkota.go.id/index.php/informasi/pegawai_jabatan/get_so_dropdown/" + '+str(id) +
                   ',dataType: "json",success: function (data) {$.each(data.so, function (i, so) {$("#so").append($("<option></option>").val(so.id_struktur_organisasi).html(so.keterangan));});$("#so").select2("val", '+str(id_so)+');}});')
    console.append('$.ajax({url: "http://simpeg.malangkota.go.id/index.php/informasi/pegawai_jabatan/get_uniti_dropdown/" + '+str(id_so) +
                   ',dataType: "json",success: function (data) {$.each(data.uniti, function (i, uniti) {$("#uniti").append($("<option></option>").val(uniti.id_uniti).html(uniti.keterangan));});$("#uniti").select2("val", '+str(id_uniti)+');}});')
    console.append('$.ajax({url: "http://simpeg.malangkota.go.id/index.php/informasi/pegawai_jabatan/get_unitk_dropdown/" + '+str(id_uniti)+' + "/" + '+str(id_so) +
                   ',dataType: "json",success: function (data) {$.each(data.unitk, function (i, unitk) {$("#unitk").append($("<option></option>").val(unitk.id_unitk).html(unitk.keterangan));});$("#unitk").select2("val", '+str(id_unitk)+');}});')
    console.append('$.ajax({url: "http://simpeg.malangkota.go.id/index.php/informasi/pegawai_jabatan/get_sub_unitk_dropdown/" + '+str(id_unitk)+' + "/" + '+str(id_so) +
                   ',dataType: "json",success: function (data) {$.each(data.unitk, function (i, unitk) {$("#sub_unitk").append($("<option></option>").val(unitk.id_sub_unitk).html(unitk.keterangan));});}});')
    console.append(
        '$("#so").empty().append("<option value=\'0\'>- -</option>").removeAttr("disabled");')
    console.append(
        '$("#uniti").empty().append("<option value=\'0\'>- -</option>").removeAttr("disabled");')
    console.append(
        '$("#unitk").empty().append("<option value=\'0\'>- -</option>").removeAttr("disabled");')
    console.append(
        '$("#sub_unitk").empty().append("<option value=\'0\'>- -</option>").removeAttr("disabled");')
    console.append(
        '$("#atasan_pp").empty().append("<option value=\'0\'>- -</option>").removeAttr("disabled");')

    for i in range(len(console)):
        driver.execute_script(console[i])

# %%
