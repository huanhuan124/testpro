import yaml
import pytest
class TestYaml:


    # def test_demo(self,a,b):
    #     print(a+b)


   # ya = yaml.safe_load(file("./data/data.yaml"))


    def test_yaml(self):
        # f = open("./data/data.yaml", encoding="utf-8")
        # f = open("./data/data1.yaml", encoding="utf-8")
        # ya = yaml.load(f)
        # print(ya)
        #打印出yaml文件中的内容
        print(yaml.safe_load(open("./data/data2.yaml")))


    @pytest.mark.parametrize(["a","b"], yaml.safe_load(open("./data/data1.yaml")))
    def test_pyyaml(self,a,b):
        print(a+b)


    @pytest.mark.parametrize("env",yaml.safe_load(open("./data/data.yaml")))
    def test_env(self,env):
        if "test" in env:
            print("这是测试环境")
            print(yaml.safe_load(open("./data/data.yaml")))
            print(type(env))
            print(env)
            # print(env['test'])
        elif "dev" in env:
            print("这是开发环境")


