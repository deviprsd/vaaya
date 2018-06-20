package com.vaaya.shraavani.vaaya

import android.content.Intent
import android.os.Bundle
import android.support.design.widget.NavigationView
import android.support.design.widget.Snackbar
import android.support.v4.app.Fragment
import android.support.v4.view.GravityCompat
import android.support.v7.app.ActionBarDrawerToggle
import android.util.Log
import android.view.MenuItem
import android.widget.Toast
import com.vaaya.shraavani.vaaya.master.VaayaActivity
import kotlinx.android.synthetic.main.activity_home.*
import kotlinx.android.synthetic.main.app_bar_home.*
import kotlinx.android.synthetic.main.content_home.*

class HomeActivity : VaayaActivity(), NavigationView.OnNavigationItemSelectedListener {

    private val TIME_INTERVAL = 2000 // # milliseconds, desired time passed between two back presses.
    private var mBackPressed: Long = 0

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_home)
        setSupportActionBar(toolbar)

        fab.setOnClickListener { view ->
            Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
                    .setAction("Action", null).show()
        }

        val toggle = ActionBarDrawerToggle(
                this, drawer_layout, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close)
        drawer_layout.addDrawerListener(toggle)
        toggle.syncState()

        nav_view.setNavigationItemSelectedListener(this)

        supportFragmentManager.addOnBackStackChangedListener {
            Log.i("testing", getCurrentFragment().tag)
        }
    }

    override fun onBackPressed() {
        if (drawer_layout.isDrawerOpen(GravityCompat.START)) {
            drawer_layout.closeDrawer(GravityCompat.START)
        } else {
            if (mBackPressed + TIME_INTERVAL > System.currentTimeMillis()) {
                super.onBackPressed()
                return
            } else {
                Toast.makeText(baseContext, "Tap back button in order to exit", Toast.LENGTH_SHORT).show()
            }

            mBackPressed = System.currentTimeMillis()
        }
    }

    override fun onNavigationItemSelected(item: MenuItem): Boolean {
        if(item.groupId == R.id.vaaya_nav_primary) title = item.title

        when (item.itemId) {
            R.id.vaaya_nav_stats -> replace(ProgressFragment.newInstance())
            R.id.vaaya_nav_calendar -> replace(CalendarFragment.newInstance())
            R.id.vaaya_nav_suggestions -> replace(HabitsFragment.newInstance())
            R.id.vaaya_nav_help -> replace(HelpFragment.newInstance())
            R.id.vaaya_nav_settings -> replace(SettingsFragment.newInstance())
            R.id.vaaya_nav_about -> startActivity(Intent(this@HomeActivity, AboutActivity::class.java))
            R.id.vaaya_nav_logout -> logout()
        }

        drawer_layout.closeDrawer(GravityCompat.START)
        return true
    }

    private fun getFragmentCount(): Int {
        return supportFragmentManager.backStackEntryCount
    }

    private fun getFragmentAt(index: Int): Fragment {
        return supportFragmentManager.findFragmentByTag(index.toString())
    }

    private fun getCurrentFragment(): Fragment {
        return getFragmentAt(getFragmentCount() - 1)
    }

    private fun replace(fragment: Fragment) {
        supportFragmentManager.beginTransaction()
                .replace(
                        vaaya_home_page_layout.id,
                        fragment,
                        getFragmentCount().toString()
                )
                .commit()
    }
}
