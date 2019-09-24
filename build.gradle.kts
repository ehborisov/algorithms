
allprojects {
    apply(plugin = "java")
    group = "com.ehborisov.algorithms"

    version = "1.0"

    repositories {
        jcenter()
        mavenCentral()
    }

    dependencies {
        "compile"("com.google.guava:guava:11.0.2")
        "compile"("org.slf4j:slf4j-simple:1.7.28")
        "testCompile"("junit:junit:4.4")
    }
}
