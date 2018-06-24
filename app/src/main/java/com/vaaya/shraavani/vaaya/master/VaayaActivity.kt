package com.vaaya.shraavani.vaaya.master

import android.annotation.SuppressLint
import android.content.Intent
import android.content.pm.ActivityInfo
import android.content.res.Resources
import android.os.Bundle
import android.support.v7.app.AppCompatActivity
import android.transition.Slide
import com.vaaya.shraavani.vaaya.HomeActivity
import com.vaaya.shraavani.vaaya.LoginActivity
import com.vaaya.shraavani.vaaya.R
import com.vaaya.shraavani.vaaya.WelcomeActivity
import com.vaaya.shraavani.vaaya.model.Settings
import io.realm.Realm
import java.io.IOException
import java.util.*
import kotlin.concurrent.schedule




@SuppressLint("Registered")
open class VaayaActivity: AppCompatActivity() {

    lateinit var realm: Realm

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        requestedOrientation = ActivityInfo.SCREEN_ORIENTATION_PORTRAIT

        realm = Realm.getDefaultInstance()

        val slide = Slide()
        slide.duration = 1000
        window.exitTransition = slide
        window.enterTransition = slide
    }

    protected fun runController() {
        val settings = realm.where(Settings::class.java)
        if(settings.count() <= 7L) {
            realm.executeTransaction { it ->
                it.delete(Settings::class.java)
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

        val runFirstTime = realm.where(Settings::class.java)
                .equalTo("key", "run_first_time").findFirst()
        val apiKey = realm.where(Settings::class.java)
                .beginsWith("key", "api_key").findAll().sort("key")
        if(runFirstTime!!.settings.equals("true", true)) {
            Timer().schedule(2000) {
                startActivity(Intent(this@VaayaActivity, WelcomeActivity::class.java))
            }
        } else if(apiKey[0]?.settings == null || apiKey[1]?.settings!!.toLong() < System.currentTimeMillis()) {
            startActivity(Intent(this@VaayaActivity, LoginActivity::class.java))
        } else {
            /*realm.executeTransaction {
                runFirstTime.settings = "true"
            }*/
            finishAffinity()
            startActivity(Intent(this@VaayaActivity, HomeActivity::class.java))
        }
    }

    protected fun logout() {
        val api = realm.where(Settings::class.java).beginsWith("key", "api_key").findAll()
        realm.executeTransaction{ _ ->
            api.forEach {
                it.settings = null
            }
        }
        runController()
    }

    fun convertPixelsToDp(px: Float): Float {
        return Math.round(px / (Resources.getSystem().getDisplayMetrics().densityDpi / 160f)).toFloat()
    }

    fun convertDpToPixel(dp: Float): Float {
        return Math.round(dp * (Resources.getSystem().getDisplayMetrics().densityDpi / 160f)).toFloat()
    }

    override fun onDestroy() {
        super.onDestroy()
        realm.close()
    }

}