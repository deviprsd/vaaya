package com.vaaya.shraavani.vaaya

import android.content.Intent
import android.os.Bundle
import android.support.v4.app.Fragment
import android.support.v4.app.FragmentManager
import android.support.v4.app.FragmentStatePagerAdapter
import android.support.v4.view.ViewPager
import android.text.Html
import android.transition.TransitionManager
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import com.vaaya.shraavani.vaaya.master.VaayaActivity
import com.vaaya.shraavani.vaaya.model.Settings
import io.realm.Realm
import kotlinx.android.synthetic.main.activity_welcome.*
import kotlinx.android.synthetic.main.fragment_welcome.view.*



class WelcomeActivity : VaayaActivity() {

    private var mSectionsPagerAdapter: SectionsPagerAdapter? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_welcome)

        mSectionsPagerAdapter = SectionsPagerAdapter(supportFragmentManager)
        container.adapter = mSectionsPagerAdapter
        indicator.setupWithViewPager(container, true)

        container.addOnPageChangeListener(WelcomePageListener())
        tour_done.setOnClickListener { _ ->
            val realm = Realm.getDefaultInstance()
            val runFirstTime = realm.where(Settings::class.java)
                    .equalTo("key", "run_first_time").findFirst()!!
            realm.executeTransaction {
                runFirstTime.settings = "false"
            }
            startActivity(Intent(this@WelcomeActivity, HomeActivity::class.java))
        }
    }

    override fun onBackPressed() {
        return
    }

    inner class SectionsPagerAdapter(fm: FragmentManager) : FragmentStatePagerAdapter(fm) {

        val texts = arrayOf(
                "Welcome to <br><b>Vaaya</b>",
                "We will <b>help</b> you track <b><i>Emotions</i></b>",
                "<u>Balance</u> them <b>OUT</b>",
                "And form <u><b><i>new Habits</i></b></u>"
        )

        override fun getItem(position: Int): Fragment {
            return WelcomeFragment.newInstance(texts[position])
        }

        override fun getCount(): Int {
            return 4
        }
    }

    inner class WelcomePageListener(): ViewPager.SimpleOnPageChangeListener() {
        override fun onPageSelected(position: Int) {
            TransitionManager.beginDelayedTransition(welcome_main_content)
            when(position) {
                in 0..2 -> {
                    if(indicator.visibility != View.VISIBLE) {
                        indicator.visibility = View.VISIBLE
                    }
                    if(tour_done.visibility != View.GONE) {
                        tour_done.visibility = View.GONE
                    }
                }
                3 -> {
                    indicator.visibility = View.GONE
                    tour_done.visibility = View.VISIBLE
                }
            }
        }
    }

    @Suppress("DEPRECATION")
    class WelcomeFragment : Fragment() {

        override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?,
                                  savedInstanceState: Bundle?): View? {
            val rootView = inflater.inflate(R.layout.fragment_welcome, container, false)
            rootView.section_label.text = Html.fromHtml(arguments?.getString(ARG_TEXT))
            return rootView
        }

        companion object {
            private val ARG_TEXT = "section_text"

            fun newInstance(text: String): WelcomeFragment {
                val fragment = WelcomeFragment()
                val args = Bundle()
                args.putString(ARG_TEXT, text)
                fragment.arguments = args
                return fragment
            }
        }
    }
}
