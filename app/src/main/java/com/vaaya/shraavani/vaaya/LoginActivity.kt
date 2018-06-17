package com.vaaya.shraavani.vaaya

import android.os.Bundle
import android.support.design.widget.Snackbar
import com.vaaya.shraavani.vaaya.master.VaayaActivity
import com.vaaya.shraavani.vaaya.model.Settings
import kotlinx.android.synthetic.main.activity_login.*
import org.json.JSONObject
import java.util.*

class LoginActivity : VaayaActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)

        vaaya_login_btn.setOnClickListener {
            login()
        }
    }

    private fun login() {
        if (!vaaya_login_email.text.isEmpty() && !vaaya_login_password.text.isEmpty()) {
            checkLogin(vaaya_login_email.text.toString(), vaaya_login_password.text.toString())
        } else {
            Snackbar.make(vaaya_login_layout, "C'mon, enter some credentials", Snackbar.LENGTH_LONG).show()
        }
    }

    private fun checkLogin(user: String, password: String) {
        val credentials = JSONObject(realm.where(Settings::class.java)
                .equalTo("key", "dummy_login").findFirst()!!.settings)
        if (credentials["user"] == user && credentials["password"] == password) {
            val api = realm.where(Settings::class.java).beginsWith("key", "api_key").findAll().sort("key")
            realm.executeTransaction {
                api[0]?.settings = UUID.randomUUID().toString()
                api[1]?.settings = System.currentTimeMillis().plus(3600000L * 24 * 30).toString()
            }
            runController()
        } else {
            Snackbar.make(vaaya_login_layout, "Ooops, bad credentials. If it's not you don't invade privacy", Snackbar.LENGTH_LONG).show()
        }
    }
}
