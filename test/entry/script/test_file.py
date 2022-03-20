import codecs
import os

import pytest

from jentry.entry.script import load_entries_from_file, load_entry_classes_from_code
from ...testing import demo_mark, DEMO_PROJECT_PATH, demo_complex_mark, DEMO_COMPLEX_PROJECT_PATH


class TestEntryScriptProject:
    @demo_mark
    def test_load_entries_from_file_demo(self):
        entries = list(load_entries_from_file(os.path.join(DEMO_PROJECT_PATH, 'src/homework/Main.java')))
        assert len(entries) == 1

        entry = entries[0]
        assert entry.package == 'homework'
        assert entry.clazz == 'Main'

    @demo_complex_mark
    def test_load_entries_from_file_demo_complex(self):
        entries = list(load_entries_from_file(os.path.join(DEMO_COMPLEX_PROJECT_PATH, 'src/Main.java')))
        assert len(entries) == 1

        entry = entries[0]
        assert entry.package is None
        assert entry.clazz == 'Main'

    @demo_mark
    def test_load_entry_classes_from_code_demo(self):
        with codecs.open(os.path.join(DEMO_PROJECT_PATH, 'src/homework/Main.java'), 'r') as sf:
            classes = list(load_entry_classes_from_code(sf.read()))

            assert len(classes) == 1
            clx = classes[0]
            assert clx == ('homework', 'Main')

    @demo_complex_mark
    def test_load_entry_classes_from_code_demo_complex(self):
        with codecs.open(os.path.join(DEMO_COMPLEX_PROJECT_PATH, 'src/Main.java'), 'r') as sf:
            classes = list(load_entry_classes_from_code(sf.read()))

            assert len(classes) == 1
            clx = classes[0]
            assert clx == (None, 'Main')

    @pytest.mark.unittest
    def test_load_entry_classes_from_code_hdl(self):
        hdl_code = """
package homework;

import homework.expression.core.interfaces.Expression;
import homework.expression.parse.ExpParser;
import homework.tri.TriProdTermTree;

import java.io.InputStream;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        System.out.println(getAns(System.in));
    }

    static String getAns(InputStream stream) {
        return getAns(stream, false);
    }

    static String getAns(InputStream stream, boolean debug) {
        Scanner scanner = new Scanner(stream);
        String line;
        if (scanner.hasNextLine()) {
            line = scanner.nextLine();
        } else {
            line = "";
        }
        return getAns(line, debug);
    }

    private static String getAns(String line) {
        return getAns(line, false);
    }

    static String getAns(String line, boolean debug) {
        Expression exp = ExpParser.getInstance().parseExp(line, debug);
        if (debug) {
            System.out.println("Main.getAns:");
            System.out.println("input exp = " + exp);
        }
        if (exp == null) {
            return "WRONG FORMAT!";
        }
        exp = exp.diff();
        if (debug) {
            System.out.println("Main.getAns:");
            System.out.println("diff exp = " + exp);
        }
        return ((TriProdTermTree) exp.compute(new TriProdTermTree()))
            .toTriExp().toString();
    }
}

        """

        classes = list(load_entry_classes_from_code(hdl_code))

        assert len(classes) == 1
        clx = classes[0]
        assert clx == ('homework', 'Main')

    @pytest.mark.unittest
    def test_load_entry_classes_from_code_with_extra_name(self):
        expected_code = """
package src;

import com.oocourse.elevator2.ElevatorInput;
import com.oocourse.elevator2.PersonRequest;

class Main {
    public static void main(String[] argc) throws Exception {
        ElevatorInput elevatorInput = new ElevatorInput(System.in);
        Elev e = new Elev();
        e.start();
        while (true) {
            PersonRequest request1 = elevatorInput.nextPersonRequest();
            if (request1 == null) {
                e.getJudge2();
                elevatorInput.close();
                return;
            }
            Person request = new Person(request1.getFromFloor(),
                    request1.getToFloor(), request1.getPersonId());
            e.add(request);
        }
    }
}
        """

        classes = list(load_entry_classes_from_code(expected_code))

        assert len(classes) == 1
        clx = classes[0]
        assert clx == ('src', 'Main')

    @pytest.mark.unittest
    def test_load_entry_classes_from_code_with_ellipse(self):
        expected_code = """
        package src;

        import com.oocourse.elevator2.ElevatorInput;
        import com.oocourse.elevator2.PersonRequest;

        class Main {
            public static void main(String... argc) throws Exception {
                ElevatorInput elevatorInput = new ElevatorInput(System.in);
                Elev e = new Elev();
                e.start();
                while (true) {
                    PersonRequest request1 = elevatorInput.nextPersonRequest();
                    if (request1 == null) {
                        e.getJudge2();
                        elevatorInput.close();
                        return;
                    }
                    Person request = new Person(request1.getFromFloor(),
                            request1.getToFloor(), request1.getPersonId());
                    e.add(request);
                }
            }
        }
                """

        classes = list(load_entry_classes_from_code(expected_code))

        assert len(classes) == 1
        clx = classes[0]
        assert clx == ('src', 'Main')
