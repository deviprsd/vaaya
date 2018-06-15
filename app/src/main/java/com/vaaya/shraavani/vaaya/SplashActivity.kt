package com.vaaya.shraavani.vaaya

import android.content.Intent
import android.os.Bundle
import android.util.Log
import com.vaaya.shraavani.vaaya.master.VaayaActivity
import com.vaaya.shraavani.vaaya.model.Settings
import io.realm.Realm
import java.io.IOException
import java.util.*
import kotlin.concurrent.schedule

class SplashActivity : VaayaActivity() {

    private lateinit var realm: Realm

    override fun onCreate(savedInstanceState: Bundle?) {
        // setTheme(R.style.VaayaTheme_NoActionBar)
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_splash)
        realm = Realm.getDefaultInstance()
    }

    override fun onResume() {
        super.onResume()
        isRunForFirstTime()
    }

    private fun isRunForFirstTime() {
        val settings = realm.where(Settings::class.java)
        if(settings.count() == 0L) {
            realm.executeTransaction { it ->
                try {
                    it.createAllFromJson(
                            Settings::class.java,
                            resources.openRawResource(R.raw.settings_default)
                    )
                } catch (e: IOException) {
                    throw RuntimeException(e)
                }
            }
        }

        val runFirstTime = settings.equalTo("key", "run_first_time").findFirst()
        if(runFirstTime!!.settings.equals("true", true)) {
            Log.i("Welcome", true.toString())
            Timer().schedule(2000) {
                startActivity(Intent(this@SplashActivity, WelcomeActivity::class.java))
            }
            realm.executeTransaction {
                runFirstTime.settings = "false"
            }
        } else {
            realm.executeTransaction {
                runFirstTime.settings = "true"
            }
            startActivity(Intent(this@SplashActivity, HomeActivity::class.java))
        }
    }

    override fun onDestroy() {
        super.onDestroy()
        realm.close()
    }
}
