import React, { useState, useEffect, useRef } from 'react';
import { Star, Download, Mail, Phone, MapPin, Calendar, GraduationCap, Menu, X, Apple } from 'lucide-react';
import portfolioData from './portfolio_data.json';

interface App {
  id: string;
  name: string;
  category: string;
  description: string;
  rating: number;
  downloads: string;
  price: string;
  icon_url: string;
  screenshots: number;
  app_store_url: string;
}

interface Experience {
  id: number;
  title: string;
  company: string;
  period: string;
  description: string;
}

interface Skill {
  name: string;
  level: number;
}

const apps: App[] = portfolioData.apps;
const experiences: Experience[] = portfolioData.experiences;
const skills: Skill[] = portfolioData.skills;

export default function Portfolio() {
  const [selectedCategory, setSelectedCategory] = useState('All');
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [selectedApp, setSelectedApp] = useState<App | null>(null);
  const [activeSection, setActiveSection] = useState('hero');

  const heroRef = useRef<HTMLElement>(null);
  const appsRef = useRef<HTMLElement>(null);
  const cvRef = useRef<HTMLElement>(null);
  const contactRef = useRef<HTMLElement>(null);

  const categories = ['All', ...Array.from(new Set(apps.map(app => app.category)))];

  const filteredApps = selectedCategory === 'All'
    ? apps
    : apps.filter(app => app.category === selectedCategory);

  const scrollToSection = (ref: React.RefObject<HTMLElement | null>, sectionName: string) => {
    ref.current?.scrollIntoView({ behavior: 'smooth' });
    setMobileMenuOpen(false);
  };

  useEffect(() => {
    const handleScroll = () => {
      const scrollPosition = window.scrollY + 100;

      const sections = [
        { ref: heroRef, name: 'hero' },
        { ref: appsRef, name: 'apps' },
        { ref: cvRef, name: 'cv' },
        { ref: contactRef, name: 'contact' }
      ];

      for (const section of sections) {
        if (section.ref.current) {
          const { offsetTop, offsetHeight } = section.ref.current;
          if (scrollPosition >= offsetTop && scrollPosition < offsetTop + offsetHeight) {
            setActiveSection(section.name);
            break;
          }
        }
      }
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const renderStars = (rating: number) => {
    return Array.from({ length: 5 }, (_, i) => (
      <Star
        key={i}
        className={`w-4 h-4 ${i < Math.floor(rating) ? 'fill-yellow-400 text-yellow-400' : 'text-gray-300'}`}
      />
    ));
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100">
      {/* Header */}
      <header className="bg-white shadow-sm sticky top-0 z-40">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            <div className="flex items-center space-x-2">
              <Apple className="w-8 h-8 text-gray-900" />
              <span className="text-xl font-bold text-gray-900">iOS Portfolio</span>
            </div>

            {/* Desktop Navigation */}
            <nav className="hidden md:flex space-x-8">
              <button
                onClick={() => scrollToSection(heroRef, 'hero')}
                className={`text-sm font-medium transition-colors ${
                  activeSection === 'hero' ? 'text-blue-600' : 'text-gray-700 hover:text-blue-600'
                }`}
              >
                Home
              </button>
              <button
                onClick={() => scrollToSection(appsRef, 'apps')}
                className={`text-sm font-medium transition-colors ${
                  activeSection === 'apps' ? 'text-blue-600' : 'text-gray-700 hover:text-blue-600'
                }`}
              >
                Apps
              </button>
              <button
                onClick={() => scrollToSection(cvRef, 'cv')}
                className={`text-sm font-medium transition-colors ${
                  activeSection === 'cv' ? 'text-blue-600' : 'text-gray-700 hover:text-blue-600'
                }`}
              >
                CV
              </button>
              <button
                onClick={() => scrollToSection(contactRef, 'contact')}
                className={`text-sm font-medium transition-colors ${
                  activeSection === 'contact' ? 'text-blue-600' : 'text-gray-700 hover:text-blue-600'
                }`}
              >
                Contact
              </button>
            </nav>

            {/* Mobile menu button */}
            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="md:hidden p-2 rounded-md text-gray-700 hover:bg-gray-100"
            >
              {mobileMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
            </button>
          </div>
        </div>

        {/* Mobile Navigation */}
        {mobileMenuOpen && (
          <div className="md:hidden bg-white border-t">
            <div className="px-2 pt-2 pb-3 space-y-1">
              <button
                onClick={() => scrollToSection(heroRef, 'hero')}
                className={`block w-full text-left px-3 py-2 rounded-md text-base font-medium ${
                  activeSection === 'hero' ? 'bg-blue-50 text-blue-600' : 'text-gray-700 hover:bg-gray-50'
                }`}
              >
                Home
              </button>
              <button
                onClick={() => scrollToSection(appsRef, 'apps')}
                className={`block w-full text-left px-3 py-2 rounded-md text-base font-medium ${
                  activeSection === 'apps' ? 'bg-blue-50 text-blue-600' : 'text-gray-700 hover:bg-gray-50'
                }`}
              >
                Apps
              </button>
              <button
                onClick={() => scrollToSection(cvRef, 'cv')}
                className={`block w-full text-left px-3 py-2 rounded-md text-base font-medium ${
                  activeSection === 'cv' ? 'bg-blue-50 text-blue-600' : 'text-gray-700 hover:bg-gray-50'
                }`}
              >
                CV
              </button>
              <button
                onClick={() => scrollToSection(contactRef, 'contact')}
                className={`block w-full text-left px-3 py-2 rounded-md text-base font-medium ${
                  activeSection === 'contact' ? 'bg-blue-50 text-blue-600' : 'text-gray-700 hover:bg-gray-50'
                }`}
              >
                Contact
              </button>
            </div>
          </div>
        )}
      </header>

      {/* Hero Section */}
      <section ref={heroRef} className="bg-gradient-to-r from-blue-600 to-purple-600 text-white py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <h1 className="text-4xl md:text-5xl font-bold mb-4">
              iOS Developer & App Creator
            </h1>
            <p className="text-xl mb-8 text-blue-100">
              Crafting exceptional mobile experiences with passion and precision
            </p>
            <div className="flex justify-center space-x-4">
              <button
                onClick={() => scrollToSection(appsRef, 'apps')}
                className="bg-white text-blue-600 px-6 py-3 rounded-lg font-semibold hover:bg-gray-100 transition-colors"
              >
                View Apps
              </button>
              <button
                onClick={() => scrollToSection(cvRef, 'cv')}
                className="border-2 border-white text-white px-6 py-3 rounded-lg font-semibold hover:bg-white hover:text-blue-600 transition-colors"
              >
                View CV
              </button>
            </div>
          </div>
        </div>
      </section>

      {/* Apps Section */}
      <section ref={appsRef} className="py-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="mb-8">
            <h2 className="text-3xl font-bold text-gray-900 mb-2">Featured Apps</h2>
            <p className="text-gray-600">Discover my iOS applications available on the App Store</p>
          </div>

          {/* Category Filter */}
          <div className="flex flex-wrap gap-2 mb-8">
            {categories.map(category => (
              <button
                key={category}
                onClick={() => setSelectedCategory(category)}
                className={`px-4 py-2 rounded-full text-sm font-medium transition-colors ${
                  selectedCategory === category
                    ? 'bg-blue-600 text-white'
                    : 'bg-white text-gray-700 hover:bg-gray-100 border border-gray-300'
                }`}
              >
                {category}
              </button>
            ))}
          </div>

          {/* Apps Grid */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {filteredApps.map(app => (
              <div
                key={app.id}
                onClick={() => setSelectedApp(app)}
                className="bg-white rounded-xl shadow-lg hover:shadow-xl transition-shadow cursor-pointer overflow-hidden"
              >
                <div className="p-6">
                  <div className="flex items-start justify-between mb-4">
                    <img src={app.icon_url} alt={app.name} className="w-12 h-12 rounded-lg" />
                    <span className="bg-green-100 text-green-800 text-xs font-medium px-2.5 py-0.5 rounded">
                      {app.price || 'Free'}
                    </span>
                  </div>
                  <h3 className="text-xl font-semibold text-gray-900 mb-2">{app.name}</h3>
                  <p className="text-sm text-gray-600 mb-1">{app.category}</p>
                  <p className="text-gray-700 text-sm mb-4 line-clamp-2">{app.description}</p>
                  <div className="flex items-center justify-between">
                    <div className="flex items-center space-x-1">
                      {renderStars(app.rating)}
                      <span className="text-sm text-gray-600 ml-1">{app.rating}</span>
                    </div>
                    <div className="flex items-center text-sm text-gray-600">
                      <Download className="w-4 h-4 mr-1" />
                      {app.downloads}
                    </div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CV Section */}
      <section ref={cvRef} className="py-16 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="mb-8">
            <h2 className="text-3xl font-bold text-gray-900 mb-2">Curriculum Vitae</h2>
            <p className="text-gray-600">Professional experience and skills</p>
          </div>

          <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
            {/* Personal Info */}
            <div className="lg:col-span-1">
              <div className="bg-white rounded-xl shadow-lg p-6 mb-6">
                <h3 className="text-xl font-semibold text-gray-900 mb-4">Personal Information</h3>
                <div className="space-y-3">
                  <div className="flex items-center space-x-3">
                    <Mail className="w-5 h-5 text-gray-400" />
                    <span className="text-gray-700">john.doe@example.com</span>
                  </div>
                  <div className="flex items-center space-x-3">
                    <Phone className="w-5 h-5 text-gray-400" />
                    <span className="text-gray-700">+1 (555) 123-4567</span>
                  </div>
                  <div className="flex items-center space-x-3">
                    <MapPin className="w-5 h-5 text-gray-400" />
                    <span className="text-gray-700">San Francisco, CA</span>
                  </div>
                  <div className="flex items-center space-x-3">
                    <Calendar className="w-5 h-5 text-gray-400" />
                    <span className="text-gray-700">Available for hire</span>
                  </div>
                </div>
              </div>

              {/* Education */}
              <div className="bg-white rounded-xl shadow-lg p-6">
                <h3 className="text-xl font-semibold text-gray-900 mb-4">Education</h3>
                <div className="flex items-start space-x-4">
                  <GraduationCap className="w-6 h-6 text-gray-400 mt-1" />
                  <div>
                    <h4 className="font-semibold text-gray-900">Bachelor of Science in Computer Science</h4>
                    <p className="text-gray-600">Stanford University</p>
                    <p className="text-sm text-gray-500 mt-1">2014 - 2018</p>
                  </div>
                </div>
              </div>
            </div>

            {/* Experience and Skills */}
            <div className="lg:col-span-2 space-y-6">
              {/* Experience */}
              <div className="bg-white rounded-xl shadow-lg p-6">
                <h3 className="text-xl font-semibold text-gray-900 mb-4">Work Experience</h3>
                <div className="space-y-6">
                  {experiences.map(exp => (
                    <div key={exp.id} className="border-l-2 border-blue-600 pl-4 relative">
                      <div className="absolute w-3 h-3 bg-blue-600 rounded-full -left-2 top-0"></div>
                      <div className="flex items-start justify-between mb-2">
                        <div>
                          <h4 className="font-semibold text-gray-900">{exp.title}</h4>
                          <p className="text-gray-600">{exp.company}</p>
                        </div>
                        <span className="text-sm text-gray-500">{exp.period}</span>
                      </div>
                      <p className="text-gray-700 text-sm">{exp.description}</p>
                    </div>
                  ))}
                </div>
              </div>

              {/* Skills */}
              <div className="bg-white rounded-xl shadow-lg p-6">
                <h3 className="text-xl font-semibold text-gray-900 mb-4">Technical Skills</h3>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  {skills.map(skill => (
                    <div key={skill.name}>
                      <div className="flex justify-between mb-1">
                        <span className="text-sm font-medium text-gray-700">{skill.name}</span>
                        <span className="text-sm text-gray-600">{skill.level}%</span>
                      </div>
                      <div className="w-full bg-gray-200 rounded-full h-2">
                        <div
                          className="bg-gradient-to-r from-blue-500 to-purple-500 h-2 rounded-full transition-all"
                          style={{ width: `${skill.level}%` }}
                        ></div>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Contact Section */}
      <section ref={contactRef} className="py-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-8">
            <h2 className="text-3xl font-bold text-gray-900 mb-2">Get In Touch</h2>
            <p className="text-gray-600">Let's discuss your next iOS project</p>
          </div>
          <div className="max-w-2xl mx-auto">
            <div className="bg-white rounded-xl shadow-lg p-8">
              <form className="space-y-6">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">Name</label>
                  <input
                    type="text"
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                    placeholder="Your Name"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">Email</label>
                  <input
                    type="email"
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                    placeholder="your@email.com"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">Message</label>
                  <textarea
                    rows={4}
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                    placeholder="Your message..."
                  ></textarea>
                </div>
                <button
                  type="submit"
                  className="w-full bg-gradient-to-r from-blue-600 to-purple-600 text-white py-3 rounded-lg font-semibold hover:from-blue-700 hover:to-purple-700 transition-colors"
                >
                  Send Message
                </button>
              </form>
            </div>
          </div>
        </div>
      </section>

      {/* App Detail Modal */}
      {selectedApp && (
        <div
          className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50"
          onClick={() => setSelectedApp(null)}
        >
          <div
            className="bg-white rounded-xl max-w-2xl w-full max-h-screen overflow-y-auto"
            onClick={(e) => e.stopPropagation()}
          >
            <div className="p-6">
              <div className="flex justify-between items-start mb-4">
                <div className="flex items-center space-x-4">
                  <img src={selectedApp.icon_url} alt={selectedApp.name} className="w-16 h-16 rounded-lg" />
                  <div>
                    <h3 className="text-2xl font-bold text-gray-900">{selectedApp.name}</h3>
                    <p className="text-gray-600">{selectedApp.category}</p>
                  </div>
                </div>
                <button
                  onClick={() => setSelectedApp(null)}
                  className="p-2 hover:bg-gray-100 rounded-lg"
                >
                  <X className="w-5 h-5 text-gray-500" />
                </button>
              </div>
              <p className="text-gray-700 mb-4">{selectedApp.description}</p>
              <div className="flex items-center space-x-4 mb-6">
                <div className="flex items-center space-x-1">
                  {renderStars(selectedApp.rating)}
                  <span className="text-gray-600 ml-1">{selectedApp.rating}</span>
                </div>
                <span className="text-gray-400">|</span>
                <span className="text-gray-600">{selectedApp.downloads} downloads</span>
                <span className="text-gray-400">|</span>
                <span className="font-semibold text-gray-900">{selectedApp.price}</span>
              </div>
              <div className="mb-6">
                <h4 className="font-semibold text-gray-900 mb-3">Screenshots</h4>
                <div className="grid grid-cols-2 gap-3">
                  {Array.from({ length: selectedApp.screenshots || 3 }, (_, i) => (
                    <div key={i} className="bg-gray-200 border-2 border-dashed rounded-xl h-48" />
                  ))}
                </div>
              </div>
              <a href={selectedApp.app_store_url} target="_blank" rel="noopener noreferrer" className="w-full bg-blue-600 text-white py-3 rounded-lg font-semibold hover:bg-blue-700 transition-colors flex items-center justify-center space-x-2">
                <Download className="w-5 h-5" />
                <span>Download from App Store</span>
              </a>
            </div>
          </div>
        </div>
      )}

      {/* Footer */}
      <footer className="bg-gray-900 text-white py-8">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <p className="text-gray-400">© 2024 iOS Portfolio. All rights reserved.</p>
            <p className="text-gray-500 text-sm mt-2">Built with React, TypeScript & Tailwind CSS</p>
          </div>
        </div>
      </footer>
    </div>
  );
}
